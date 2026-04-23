from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

pdf_path = "Video_Script_Mobile_Security_ColorCoded.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.4*inch, bottomMargin=0.4*inch, leftMargin=0.5*inch, rightMargin=0.5*inch)
story = []

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'Title',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#1a1a2e'),
    spaceAfter=8,
    alignment=1,
    fontName='Helvetica-Bold'
)

section_header = ParagraphStyle(
    'SectionHeader',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=colors.HexColor('#6c3483'),
    spaceAfter=6,
    spaceBefore=10,
    fontName='Helvetica-Bold',
    backColor=colors.HexColor('#f0f0f0'),
    leftIndent=6
)

timing_style = ParagraphStyle(
    'Timing',
    parent=styles['Normal'],
    fontSize=9,
    textColor=colors.HexColor('#6c3483'),
    spaceAfter=4,
    fontName='Helvetica-Bold'
)

voiceover_style = ParagraphStyle(
    'Voiceover',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#0052cc'),
    spaceAfter=6,
    leftIndent=12
)

command_style = ParagraphStyle(
    'Command',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.white,
    spaceAfter=4,
    leftIndent=12,
    fontName='Courier',
    backColor=colors.HexColor('#cc0000')
)

action_style = ParagraphStyle(
    'Action',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#1a7d1a'),
    spaceAfter=6,
    leftIndent=12,
    fontName='Helvetica-Bold'
)

note_style = ParagraphStyle(
    'Note',
    parent=styles['Normal'],
    fontSize=9,
    textColor=colors.HexColor('#333333'),
    spaceAfter=4,
    leftIndent=12,
    fontName='Helvetica-Oblique'
)

# Title
story.append(Paragraph("Mobile Security Lab - Video Script", title_style))
story.append(Paragraph("How to Audit Your Android Phone Security Using Termux", styles['Normal']))
story.append(Spacer(1, 0.15*inch))

# Legend
story.append(Paragraph("<b>COLOR GUIDE:</b>", styles['Normal']))
story.append(Paragraph("BLUE = Your Voiceover | RED = Commands to Type | GREEN = Actions on Phone | BLACK = Notes", styles['Normal']))
story.append(Spacer(1, 0.1*inch))

# INTRO
story.append(Paragraph("[INTRO] 0:00 - 0:50 (50 seconds)", timing_style))
story.append(Paragraph("Hold on. Your Android phone is MORE powerful than a computer from 2010. Yet most people have NO IDEA how to secure it. Today, I am showing you exactly how to audit your phone's security using Termux. By the end, you will have installed security tools and scanned your entire network. Let's go.", voiceover_style))
story.append(Paragraph("Open Termux app on your phone", action_style))
story.append(Spacer(1, 0.08*inch))

# WHAT IS TERMUX
story.append(Paragraph("[SECTION 1: WHAT IS TERMUX] 0:50 - 2:20 (1:30)", timing_style))
story.append(Paragraph("First - what is Termux? Your Android phone runs Linux but Google hides the terminal. Termux unlocks it. It's a superpower. You get professional security tools that cost thousands: tcpdump (captures network traffic), nmap (scans networks), curl (tests web servers), openssh (remote access). Same tools penetration testers use. On your phone? Free.", voiceover_style))
story.append(Paragraph("Show Termux terminal on screen", action_style))
story.append(Spacer(1, 0.1*inch))

# INSTALLATION
story.append(Paragraph("[SECTION 2: INSTALL TOOLS] 2:20 - 4:45 (2:25)", timing_style))
story.append(Paragraph("Before running the security audit, we install nmap and curl. First: nmap - a network scanner. Type this command:", voiceover_style))
story.append(Paragraph("pkg install nmap", command_style))
story.append(Paragraph("Run on phone - Wait 30-60 seconds for completion", action_style))
story.append(Paragraph("Let it fully complete. Press y if asked", note_style))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("Perfect. nmap installed. Second tool: curl - tests web server security. Type:", voiceover_style))
story.append(Paragraph("pkg install curl", command_style))
story.append(Paragraph("Run on phone - Wait 30-60 seconds for completion", action_style))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("Excellent. Both tools installed. Professional-grade security software. Thousands of dollars. On your phone. Free. Now let's use them.", voiceover_style))
story.append(Spacer(1, 0.1*inch))

story.append(PageBreak())

# SECURITY AUDIT
story.append(Paragraph("[SECTION 3: SECURITY AUDIT] 4:45 - 11:00 (6:15)", timing_style))
story.append(Paragraph("Time for your first security audit. Step 1: Get your network information.", voiceover_style))
story.append(Paragraph("ifconfig", command_style))
story.append(Paragraph("Run on phone - 10-15 seconds - Look for inet with IP address", action_style))
story.append(Paragraph("Example: inet 10.74.149.96", note_style))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("Good. Now scan the network to find EVERY device connected. Step 2: Network scan.", voiceover_style))
story.append(Paragraph("nmap -sn 10.74.149.0/24", command_style))
story.append(Paragraph("Run on phone - 60-90 SECONDS FULL COMPLETION - Shows all connected devices", action_style))
story.append(Paragraph("If your network is 192.168.1.X instead, use: nmap -sn 192.168.1.0/24", note_style))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("Look at that. Every device identified. This scan costs companies thousands. You ran it on your phone.", voiceover_style))
story.append(Spacer(1, 0.06*inch))

story.append(Paragraph("Note: WiFi Users - Scan your WiFi range instead (usually 192.168.1.0/24)", command_style))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("Step 3: Test web server security. Hackers use this to find vulnerabilities.", voiceover_style))
story.append(Paragraph("curl -I https://google.com", command_style))
story.append(Paragraph("Run on phone - 15-20 seconds - Shows HTTP response headers", action_style))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("See that? Status 200. Headers control website behavior. Missing headers equals vulnerability. You just performed security research professionals use.", voiceover_style))
story.append(Spacer(1, 0.1*inch))

# SUMMARY
story.append(Paragraph("[SECTION 4: SUMMARY] 11:00 - 13:00 (2:00)", timing_style))
story.append(Paragraph("You installed professional tools. Discovered all network devices. Tested web security. Most people don't know this possible. You're ahead of 99 percent of users. Subscribe for more. Next video goes deeper into mobile security. Thank you. I'm Victor. See you next time.", voiceover_style))
story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# COMMANDS REFERENCE
story.append(Paragraph("COMMAND REFERENCE CARD", section_header))
story.append(Spacer(1, 0.08*inch))

commands_data = [
    ["COMMAND", "WHAT IT DOES", "TIMING"],
    ["ifconfig", "Display your IP address", "10 seconds"],
    ["pkg install nmap", "Install network scanner tool", "30-60 seconds"],
    ["pkg install curl", "Install web testing tool", "30-60 seconds"],
    ["nmap -sn 10.74.149.0/24", "Scan network for all devices", "60-90 seconds"],
    ["curl -I https://google.com", "Show HTTP response headers", "15 seconds"]
]

t = Table(commands_data, colWidths=[2.2*inch, 2.4*inch, 1.4*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#cc0000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ('FONTNAME', (0, 1), (-1, -1), 'Courier')
]))
story.append(t)
story.append(Spacer(1, 0.2*inch))

# RECORDING NOTES
story.append(Paragraph("RECORDING CHECKLIST", section_header))
tips_list = [
    "Total video is 13-14 minutes. Do not rush.",
    "Copy commands carefully. One typo breaks them.",
    "Let EACH command complete fully before next step.",
    "Take 5-10 second pauses between major sections.",
    "Show all output clearly. Don't scroll too fast.",
    "Read voiceover naturally. Emphasize key terms.",
    "Do 1-2 takes. Perfect is the enemy of done.",
    "Backup your files before editing.",
]

for tip in tips_list:
    story.append(Paragraph("• " + tip, styles['Normal']))

doc.build(story)
print("PDF created successfully!")
print("File: Video_Script_Mobile_Security_ColorCoded.pdf")
