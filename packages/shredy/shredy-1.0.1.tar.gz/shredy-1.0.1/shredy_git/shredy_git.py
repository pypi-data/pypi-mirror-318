import os
import sys
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
from fpdf import FPDF, XPos, YPos 
import subprocess
import base64
from typing import Dict, Optional, Tuple, List
from collections import defaultdict
import re

GITHUB_API_BASE = "https://api.github.com"

class PDF(FPDF):
    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')

class SREDGitAnalyzer:
    """
    Comprehensive Git repository analyzer for SR&ED documentation purposes.
    Generates SR&ED activity logs at your repository of choice.
    """
    
    def __init__(self, repo_owner: str, repo_name: str, year: int):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.year = year
        self.credentials = self._get_github_credentials()
        
    def get_github_commits(self) -> pd.DataFrame:
        """
        Fetch commits from GitHub using git credentials.
        Returns a DataFrame with commit information.
        """
        if not self.credentials:
            raise Exception("Could not obtain GitHub credentials")
        
        headers = {
            "Authorization": f"Basic {base64.b64encode((self.credentials['username'] + ':' + self.credentials['password']).encode()).decode()}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        url = f"{GITHUB_API_BASE}/repos/{self.repo_owner}/{self.repo_name}/commits"
       
        params = {
            "since": f"{self.year}-01-01T00:00:00Z",
            "until": f"{self.year}-12-31T23:59:59Z",
            "per_page": 100,
            "page": 1
        }
        commits = []
        
        while True:
            try:
                response = requests.get(url, headers=headers, params=params)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching commits: {e}")
                if response.status_code == 403:
                    print("Rate limit may have been exceeded or authentication failed")
                raise

            data = response.json()
            if not data:
                break

            for commit in data:
                if commit.get("commit"):
                    commits.append({
                        "author": commit["commit"]["author"]["name"],
                        "email": commit["commit"]["author"]["email"],
                        "date": commit["commit"]["author"]["date"],
                        "message": commit["commit"]["message"]
                    })

            # Check if we've reached the last page
            if 'next' not in response.links:
                break
                
            params["page"] += 1

        return pd.DataFrame(commits)

    def _get_github_credentials(self) -> Optional[Dict[str, str]]:
        """Get GitHub credentials from git credential helper."""
        try:
            process = subprocess.Popen(
                ['git', 'credential', 'fill'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output, error = process.communicate(input='protocol=https\nhost=github.com\n\n')
            
            if process.returncode != 0:
                raise Exception(f"Git credential error: {error}")
                
            credentials = dict(line.split('=', 1) for line in output.strip().split('\n') if '=' in line)
            
            if not credentials.get('username') or not credentials.get('password'):
                raise Exception("Incomplete credentials")
            return credentials
            
        except Exception as e:
            print(f"Error getting GitHub credentials: {e}")
            return None

    def analyze_commit_patterns(self, commit_data: pd.DataFrame) -> Dict:
        """
        Analyze commit patterns to identify development cycles and technical challenges.
        """
        patterns = {
            'bug_fixes': len([msg for msg in commit_data['message'] 
                            if any(word in msg.lower() for word in ['fix', 'bug', 'issue', 'patch'])]),
            'features': len([msg for msg in commit_data['message'] 
                           if any(word in msg.lower() for word in ['feat', 'feature', 'add', 'implement'])]),
            'testing': len([msg for msg in commit_data['message'] 
                          if any(word in msg.lower() for word in ['test', 'spec', 'coverage'])])
        }
        
        # Calculate development cycle metrics
        commit_data['date'] = pd.to_datetime(commit_data['date'])
        
        
        return patterns
    
    def generate_commit_matrix(self,commit_data: pd.DataFrame, year: int) -> pd.DataFrame:
        """Generate a GitHub-like contribution matrix."""
        commit_data['date_only'] = pd.to_datetime(commit_data['date']).dt.date
        commit_counts = commit_data.groupby(['author', 'date_only']).size().reset_index(name='count')

        authors = commit_counts['author'].unique()
        date_range = pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31')

        matrix = pd.DataFrame(index=authors, columns=date_range, data=0)
        for _, row in commit_counts.iterrows():
            matrix.at[row['author'], pd.to_datetime(row['date_only'])] = row['count']
        return matrix


    def calculate_active_days(self,commit_data: pd.DataFrame) -> pd.Series:
        """Calculate the number of days with commits for each contributor."""
        commit_data['date_only'] = pd.to_datetime(commit_data['date']).dt.date
        active_days = commit_data.groupby('author')['date_only'].nunique()
        return active_days

    def generate_heatmap(self,matrix: pd.DataFrame, year: int, output_path: str) -> None:
        """Generate a heatmap visualization of the contribution matrix."""
        plt.figure(figsize=(12, 6))
        sns.heatmap(matrix.fillna(0), cmap='YlGnBu', linewidths=0.5)
        plt.title(f"Commit Heatmap for {year}")
        plt.xlabel("Date")
        plt.ylabel("Contributor")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()


    def _is_cycle_start(self, commit_message: str) -> bool:
        """
        Determine if a commit message indicates the start of a new development cycle.
        """
        cycle_indicators = [
            r'sprint[\s-]start',
            r'begin[\s-]iteration',
            r'start[\s-]feature',
            r'major[\s-]update',
            r'version[\s-]\d+\.\d+'
        ]
        return any(re.search(pattern, commit_message.lower()) for pattern in cycle_indicators)

    def _extract_features(self, commit_message: str) -> set:
        """
        Extract feature identifiers from commit messages.
        """
        feature_patterns = [
            r'feat(?:ure)?[\s-:]\s*([^\n]+)',
            r'implement[\s-:]\s*([^\n]+)',
            r'add[\s-:]\s*([^\n]+)'
        ]
        
        features = set()
        for pattern in feature_patterns:
            matches = re.findall(pattern, commit_message, re.IGNORECASE)
            features.update(matches)
        
        return features

    def analyze_technical_complexity(self, commit_data: pd.DataFrame) -> Dict:
        """
        Analyze technical complexity and innovation indicators.
        """
        complexity = {
            'concurrent_development': self._analyze_concurrent_development(commit_data),
            'innovation_metrics': self._analyze_innovation_metrics(commit_data)
        }
        return complexity

    def _analyze_concurrent_development(self, commit_data: pd.DataFrame) -> Dict:
        """
        Analyze patterns of concurrent development work.
        """
        daily_commits = commit_data.set_index('date').resample('D').size()
        concurrent_work = {
            'max_daily_commits': daily_commits.max(),
            'avg_daily_commits': daily_commits.mean(),
            'days_with_multiple_authors': len(
                commit_data.groupby(pd.to_datetime(commit_data['date']).dt.date)
                .filter(lambda x: x['author'].nunique() > 1)
            )
        }
        return concurrent_work


    def _analyze_innovation_metrics(self, commit_data: pd.DataFrame) -> Dict:
        """
        Analyze metrics related to innovation and technological advancement.
        """
        innovation = {
            'new_features': len(commit_data[
                commit_data['message'].str.contains('new|feature|implement', case=False)
            ]),
            'experimental_work': len(commit_data[
                commit_data['message'].str.contains('experiment|prototype|poc', case=False)
            ]),
            'research_related': len(commit_data[
                commit_data['message'].str.contains('research|study|investigate', case=False)
            ])
        }
        return innovation
    from fpdf import FPDF, XPos, YPos  # Add XPos, YPos imports for new FPDF syntax


    def generate_sred_report(self, commit_data: pd.DataFrame, output_path: str):
        """
        Generate a comprehensive SR&ED-ready PDF report with commit appendix.
        Updated to use modern FPDF syntax and proper text wrapping.
        """
        pdf = PDF()
        pdf.set_margins(20, 20, 20)

        # Cover Page
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 24)
        pdf.ln(60)
        pdf.cell(0, 15, "SR&ED Activities Report", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 10, f"{self.repo_name}", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0, 10, f"{self.year}", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.ln(40)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 10, "Generated on: " + pd.Timestamp.now().strftime("%Y-%m-%d"), align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Table of Contents
        pdf.add_page()
        pdf.cell(0, 15, "Table of Contents", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # Store page numbers for each section
        toc_entries = {
                "1. Project Overview": None,
                "2. Development": None,
                "3. Metrics": None,
                "   3.1 Concurrent Development": None,
                "   3.2 Innovation Metrics": None,
                "4. Key Personnel That Contributed": None,
                "5. Contribution Analysis": None,
                "Appendix A: Detailed Commit History": None
                }

        # Reserve space in TOC
        toc_positions = {}
        for entry in toc_entries.keys():
            toc_positions[entry] = pdf.get_y()
            pdf.cell(0, 10, f"{entry}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.cell(0, 2, "", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Executive Summary
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 15, "Executive Summary", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 10, 
                    "This document provides supporting information for our company's SR&ED claim. " +
                    "It contains detailed analysis of our development activities, technical challenges, " +
                    "and innovations achieved during the claim period. The report includes contribution " +
                    "patterns, technical complexity metrics, and detailed commit histories from our " +
                    "development team."
                    )

        # Project Overview
        pdf.add_page()
        toc_entries["1. Project Overview"] = pdf.page_no()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 15, "1. Project Overview", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # Project details
        def add_project_detail(label: str, value: str):
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(60, 10, label, new_x=XPos.RIGHT)
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(0, 10, str(value), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        add_project_detail("Repository:", f"{self.repo_owner}/{self.repo_name}")
        add_project_detail("Project Period:", str(self.year))
        add_project_detail("Total Commits:", str(len(commit_data)))
        add_project_detail("Contributors:", str(commit_data['author'].nunique()))

        # Development Patterns
        pdf.add_page()
        toc_entries["2. Development"] = pdf.page_no()
        patterns = self.analyze_commit_patterns(commit_data)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 15, "2. Development Patterns", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)
        #Subheading
        pdf.set_font("Helvetica", "", 12)
        text1 = "In this section, we identified patterns using commit messages by our developers."

# Wrap text to fit within the margins
        page_width = pdf.w - pdf.l_margin - pdf.r_margin
        pdf.multi_cell(page_width, 10, text1, align="L")
        pdf.ln(2)

        # Create patterns table
        headers = ["Category", "Count", "Percentage"]
        data = [
                ["Bug Fixes", patterns['bug_fixes'], f"{(patterns['bug_fixes']/len(commit_data))*100:.1f}%"],
                ["New Features", patterns['features'], f"{(patterns['features']/len(commit_data))*100:.1f}%"],
                ["Testing Improvements", patterns['testing'], f"{(patterns['testing']/len(commit_data))*100:.1f}%"]
                ]

        col_widths = [80, 40, 40]

        # Table header
       # Set header font and add headers
        pdf.set_font("Helvetica", "B", 11)
        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 10, header, border=1, align="C", new_x=XPos.RIGHT if i < len(headers)-1 else XPos.LMARGIN, new_y=YPos.TOP)
        pdf.ln()

        # Add table data
        pdf.set_font("Helvetica", "", 11)
        for row in data:
            for i, cell in enumerate(row):
                pdf.cell(col_widths[i], 10, str(cell), border=1, align="L", 
                    new_x=XPos.RIGHT if i < len(row)-1 else XPos.LMARGIN,
                    new_y=YPos.NEXT if i == len(row)-1 else YPos.TOP)


        # Technical Complexity
        pdf.add_page()
        toc_entries["3. Metrics"] = pdf.page_no()
        complexity = self.analyze_technical_complexity(commit_data)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 15, "3. Metrics", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # 3.1 Concurrent Development
        toc_entries["   3.1 Concurrent Development"] = pdf.page_no()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "3.1 Concurrent Development", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        def add_metric(label: str, value: str):
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(100, 10, label + ":", new_x=XPos.RIGHT)
            pdf.set_font("Helvetica", "", 11)
            pdf.cell(0, 10, str(value), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        metrics = [
                ("Maximum Daily Commits", complexity['concurrent_development']['max_daily_commits']),
                ("Average Daily Commits", f"{complexity['concurrent_development']['avg_daily_commits']:.1f}"),
                ("Days with Multiple Contributors", complexity['concurrent_development']['days_with_multiple_authors'])
                ]

        for label, value in metrics:
            add_metric(label, value)

        # 3.2 Innovation Metrics
        pdf.ln(5)
        toc_entries["   3.2 Innovation Metrics"] = pdf.page_no()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "3.2 Innovation Metrics", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        innovation_metrics = [
                ("New Features", complexity['innovation_metrics']['new_features']),
                ("Experimental Work", complexity['innovation_metrics']['experimental_work']),
                ("Research-Related", complexity['innovation_metrics']['research_related'])
                ]

        for label, value in innovation_metrics:
            add_metric(label, value)

        # Key Personnel
        pdf.add_page()
        toc_entries["4. Key Personnel That Contributed"] = pdf.page_no()
        personnel = commit_data['author'].value_counts().to_dict()
        active_days = self.calculate_active_days(commit_data)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 15, "4. Key Personnel That Contributed", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # Personnel table
        headers = ["Contributor", "Commits", "Active Days"]
        col_widths = [80, 40, 40]

        # Table header
        pdf.set_font("Helvetica", "B", 11)
        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 10, header, border=1, new_x=XPos.RIGHT)
        pdf.ln()

        # Table data
        pdf.set_font("Helvetica", "B", 11)
        for person, commits in personnel.items():
            days_active = active_days.get(person, 0)
            pdf.cell(col_widths[0], 10, person, border=1, new_x=XPos.RIGHT)
            pdf.cell(col_widths[1], 10, str(commits), border=1, new_x=XPos.RIGHT)
            pdf.cell(col_widths[2], 10, str(days_active), border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Contribution Analysis
        pdf.add_page()
        toc_entries["5. Contribution Analysis"] = pdf.page_no()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 15, "5. Contribution Analysis", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        # Heat Map
        heatmap_path = os.path.join(os.getcwd(), f"heatmap_{self.year}.png")
        matrix = self.generate_commit_matrix(commit_data, self.year)
        self.generate_heatmap(matrix, self.year, heatmap_path)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "Contribution Matrix Heatmap:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.image(heatmap_path, x=20, y=None, w=170)
              

        # Update TOC with page numbers
        toc_page = 2  # TOC is on page 2
        for entry, page_num in toc_entries.items():
            if page_num:
                pdf.page = toc_page
                pdf.set_y(toc_positions[entry])
                pdf.cell(0, 2, str(page_num), align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Save the report
        try:
            pdf.output(output_path)
        except Exception as e:
            print(f"Error generating PDF: {str(e)}")
            raise

    def generate_appendix(self, commit_data:pd.DataFrame, report_path):
        #initialize PDF object
        pdf = PDF()
        pdf.set_margins(20, 20, 20)

        #Title
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 24)
        pdf.ln(60)
        pdf.cell(0, 15, "SR&ED Activities Report - APPENDIX", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 10, f"{self.repo_name}", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.cell(0, 10, f"{self.year}", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        contributor_length = len(commit_data['author'].value_counts())

        pdf.add_page()
        pdf.cell(0, 15, "Contributor Commits During Tax Year", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)

        author_commits = commit_data.groupby('author')

        if contributor_length < 3:
            #assumes each contributor has ~100 to 600 commits per year
            for author in sorted(commit_data['author'].unique()):
                pdf.set_font("Helvetica", "B", 14)
                pdf.set_fill_color(240, 240, 240)
                pdf.cell(0, 10, f"Contributor: {author}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.ln(2)

            author_data = author_commits.get_group(author).sort_values('date')
            pdf.set_font("Helvetica", "", 10)

            for _, commit in author_data.iterrows():
                commit_date = pd.to_datetime(commit['date']).strftime('%Y-%m-%d')
                message = commit['message']

                # Handle long messages with proper wrapping
                pdf.set_font("Helvetica", "B", 10)
                pdf.cell(30, 7, commit_date, new_x=XPos.RIGHT)

                pdf.set_font("Helvetica", "B", 10)
                effective_width = pdf.w - pdf.l_margin - pdf.r_margin - 30
                pdf.multi_cell(effective_width, 7, message)
                pdf.ln(2)

            output_path = os.path.join(os.getcwd(), f"EMPLOYEE_SREDLOG.pdf")
            try:
                    pdf.output(output_path)
            except Exception as e:
                    print(f"Error generating PDF: {str(e)}")
                    raise
            pdf.ln(5)

        if contributor_length >=3:
             for author in sorted(commit_data['author'].unique()):
                #new page per author
                newPDF = PDF()
                newPDF.add_page()
                newPDF.set_font("Helvetica", "B", 24)
                newPDF.ln(60)
                newPDF.cell(0, 15, f"SR&ED Activities Report - {author} ", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                newPDF.set_font("Helvetica", "B", 18)
                newPDF.cell(0, 10, f"{self.repo_name}", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                newPDF.cell(0, 10, f"{self.year}", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                newPDF.set_font("Helvetica", "B", 14)
                newPDF.set_fill_color(240, 240, 240)
                newPDF.cell(0, 10, f"Contributor: {author}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                newPDF.ln(2)

                author_data = author_commits.get_group(author).sort_values('date')
                newPDF.set_font("Helvetica", "", 10)

                for _, commit in author_data.iterrows():
                    commit_date = pd.to_datetime(commit['date']).strftime('%Y-%m-%d')
                    message = commit['message']

                    # Handle long messages with proper wrapping
                    newPDF.set_font("Helvetica", "B", 10)
                    newPDF.cell(30, 7, commit_date, new_x=XPos.RIGHT)

                    newPDF.set_font("Helvetica", "", 10)
                    effective_width = pdf.w - pdf.l_margin - pdf.r_margin - 30
                    newPDF.multi_cell(effective_width, 7, message)
                    newPDF.ln(2)

                sred_folder = os.path.join(os.getcwd(), "SRED_REPORT")
                if not os.path.exists(sred_folder):
                    os.makedirs(sred_folder)

                output_path = os.path.join(sred_folder, f"SREDLOG_{author}.pdf")
                try:
                    newPDF.output(output_path)
                except Exception as e:
                    print(f"Error generating PDF: {str(e)}")
                    raise
 
        

def main():
    print("Shredy starting...")
    if len(sys.argv) != 4:
        print("Usage: python analyzer.py [repo_owner] [repo_name] [year]")
        return

    repo_owner, repo_name = sys.argv[1], sys.argv[2]
    try:
        year = int(sys.argv[3])
    except ValueError:
        print("Error: Year must be a valid integer")
        return

    print(f"\nInitializing analysis for {repo_owner}/{repo_name} ({year})...")
    
    try:
        analyzer = SREDGitAnalyzer(repo_owner, repo_name, year)
        print("✓ Successfully initialized analyzer")
        
        print("\nFetching commit data from GitHub...")
        commit_data = analyzer.get_github_commits()
        print(f"✓ Successfully fetched {len(commit_data)} commits")
        
        if commit_data.empty:
            print(f"\nError: No commits found for {year}.")
            return

        print("\nAnalyzing commit patterns...")
        patterns = analyzer.analyze_commit_patterns(commit_data)
        print("✓ Completed pattern analysis")
        print(f"  - Found {patterns['features']} feature commits")
        print(f"  - Found {patterns['bug_fixes']} bug fix commits")
        
        print("\nAnalyzing technical complexity...")
        complexity = analyzer.analyze_technical_complexity(commit_data)
        print("✓ Completed complexity analysis")
        print(f"  - Analyzed {complexity['concurrent_development']['days_with_multiple_authors']} days of concurrent development")
        print(f"  - Found {complexity['innovation_metrics']['experimental_work']} experimental commits")

        print("\nGenerating SR&ED report...")
        sred_folder = os.path.join(os.getcwd(), "SRED_REPORT")
        if not os.path.exists(sred_folder):
            os.makedirs(sred_folder)
        report_path = os.path.join(sred_folder, f"sred_git_report_{year}.pdf")
        appendix_path = os.path.join(sred_folder, f"sred_git_appendix_{year}.pdf")        
        analyzer.generate_sred_report(commit_data, report_path)
        print(f"✓ Successfully generated report at: {report_path}")
        analyzer.generate_appendix(commit_data, appendix_path)
        print(f"✓ Successfully appendix report at: {appendix_path}")
        
    except Exception as e:
        print(f"\nError: An error occurred during analysis:")
        print(f"  {str(e)}")
        return

if __name__ == "__main__":
    main()
