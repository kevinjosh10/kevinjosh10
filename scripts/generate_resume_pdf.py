from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

def generate_resume():
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title / Name
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 8, "Kevin Joshua L", new_x="LMARGIN", new_y="NEXT", align="C")
    
    # Contact Info
    pdf.set_font("Helvetica", '', 10)
    pdf.cell(0, 6, "Cloud Engineer | github.com/kevinjosh10 | linkedin.com/in/kevin-josh10", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(4)
    
    # Summary
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(0, 6, "PROFESSIONAL SUMMARY", new_x="LMARGIN", new_y="NEXT")
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(2)
    
    pdf.set_font("Helvetica", '', 10)
    summary = "Cloud Infrastructure Engineer and 1st-year CS student executing a public 1000-Day Mission to master AWS Architecture and automated deployments. Focused on building scalable, serverless, and production-grade systems using infrastructure-as-code principles. High-agency builder with a bias for action and shipping real-world distributed systems."
    pdf.multi_cell(0, 5, summary)
    pdf.ln(4)
    
    # Skills
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(0, 6, "SKILLS", new_x="LMARGIN", new_y="NEXT")
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(2)
    
    pdf.set_font("Helvetica", 'B', 10)
    pdf.cell(40, 5, "Cloud & Infra:", new_x="RIGHT")
    pdf.set_font("Helvetica", '', 10)
    pdf.multi_cell(0, 5, "AWS (Lambda, API Gateway, S3, IAM, CloudWatch, VPC), Docker, Kubernetes", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", 'B', 10)
    pdf.cell(40, 5, "DevOps:", new_x="RIGHT")
    pdf.set_font("Helvetica", '', 10)
    pdf.multi_cell(0, 5, "GitHub Actions, CI/CD Pipelines, Bash Scripting, Linux System Administration", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", 'B', 10)
    pdf.cell(40, 5, "Programming:", new_x="RIGHT")
    pdf.set_font("Helvetica", '', 10)
    pdf.multi_cell(0, 5, "Python (Boto3), C++, Java, JavaScript", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("Helvetica", 'B', 10)
    pdf.cell(40, 5, "Architecture:", new_x="RIGHT")
    pdf.set_font("Helvetica", '', 10)
    pdf.multi_cell(0, 5, "Serverless Architecture, Event-Driven Systems, IoT Telemetry, Cost Optimization", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    
    # Projects
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(0, 6, "ENGINEERING PROJECTS", new_x="LMARGIN", new_y="NEXT")
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(2)
    
    projects = [
        ("CloudMorph Serverless Platform", [
            "Engineered a secure, scalable serverless file intelligence platform deployed entirely on AWS.",
            "Designed a secure backend using AWS Lambda and API Gateway to process cross-origin document uploads.",
            "Implemented pre-signed URL generation for direct-to-S3 object transfers, bypassing compute bottlenecks."
        ]),
        ("Production-Grade S3 Backup CLI Tool", [
            "Built a resilient synchronization utility for AWS S3 to automate secure, enterprise-grade backups.",
            "Developed a Python/Boto3 CLI featuring metadata-based incremental sync to reduce unnecessary network calls.",
            "Enforced AWS-native encryption and automated S3 lifecycle policies for cost-efficient, long-term archival."
        ]),
        ("EMG Sensor Firmware & IoT Architecture", [
            "Architected an end-to-end IoT monitoring solution bridging embedded hardware and cloud infrastructure.",
            "Wrote embedded C++ firmware to capture biometric data, decoupling frontend and backend services."
        ]),
        ("Cryptexa & JCE Hub", [
            "Refactored legacy monolithic web applications into highly available, modular serverless platforms.",
            "Secured API credentials using environment variable injection and automated deployments via GitHub Actions."
        ])
    ]
    
    for title, points in projects:
        pdf.set_font("Helvetica", 'B', 10)
        pdf.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", '', 10)
        for pt in points:
            pdf.cell(5, 5, "-", new_x="RIGHT")
            pdf.multi_cell(0, 5, pt, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)
        
    # Education
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(0, 6, "EDUCATION", new_x="LMARGIN", new_y="NEXT")
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(2)
    
    pdf.set_font("Helvetica", 'B', 10)
    pdf.cell(0, 5, "Jerusalem College of Engineering", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", '', 10)
    pdf.cell(0, 5, "B.E. Computer Science and Engineering | 1st Year", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    
    # Certifications
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(0, 6, "CERTIFICATIONS & INITIATIVES", new_x="LMARGIN", new_y="NEXT")
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(2)
    
    pdf.set_font("Helvetica", '', 10)
    pdf.cell(5, 5, "-", new_x="RIGHT")
    pdf.multi_cell(0, 5, "AWS Cloud Practitioner Learning Path (AWS Skill Builder)", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(5, 5, "-", new_x="RIGHT")
    pdf.multi_cell(0, 5, "The 1000-Day Cloud Mission: Publicly documented daily engineering journey mastering modern cloud stacks.", new_x="LMARGIN", new_y="NEXT")

    pdf.output("Kevin_Joshua_Resume.pdf")

if __name__ == "__main__":
    generate_resume()
