# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for NexTI Business Solutions Developer role."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_NexTI_Desarrollador.pdf"

ACCENT = colors.HexColor("#0A4D68")
TEXT = colors.HexColor("#2c2c2c")
MUTED = colors.HexColor("#555555")


def build_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=20, textColor=ACCENT, spaceAfter=2, leading=24,
        ),
        "title": ParagraphStyle(
            "Title", parent=base["Normal"], fontName="Helvetica",
            fontSize=10.5, textColor=MUTED, spaceAfter=4, leading=14,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=MUTED, spaceAfter=10, leading=13,
        ),
        "section": ParagraphStyle(
            "Section", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=11, textColor=ACCENT, spaceBefore=8, spaceAfter=4, leading=14,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=TEXT, alignment=TA_LEFT, spaceAfter=6, leading=13,
        ),
        "job_title": ParagraphStyle(
            "JobTitle", parent=base["Normal"], fontName="Helvetica-Bold",
            fontSize=10, textColor=TEXT, spaceBefore=4, spaceAfter=1, leading=13,
        ),
        "job_meta": ParagraphStyle(
            "JobMeta", parent=base["Normal"], fontName="Helvetica-Oblique",
            fontSize=9, textColor=MUTED, spaceAfter=3, leading=12,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=TEXT, leftIndent=12, spaceAfter=2, leading=13,
        ),
        "skill": ParagraphStyle(
            "Skill", parent=base["Normal"], fontName="Helvetica",
            fontSize=9.5, textColor=TEXT, spaceAfter=2, leading=13,
        ),
    }


def section_rule():
    return HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceBefore=0, spaceAfter=4)


def bullet(text, style):
    return Paragraph("\u2022 " + text, style)


def main():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm,
        topMargin=1.5 * cm, bottomMargin=1.5 * cm,
    )

    story = [
        Paragraph("JOSELYN SAAVEDRA", styles["name"]),
        Paragraph(
            "Desarrolladora de Software | C# / .NET | JavaScript / TypeScript | "
            "SQL Server | Azure DevOps",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Disponible Guayaquil (presencial) | github.com/Witch19",
            styles["contact"],
        ),
        Paragraph(
            "+593 99 252 3644 &nbsp;|&nbsp; Josytst.js@gmail.com &nbsp;|&nbsp; "
            "linkedin.com/in/joselyn-saavedra-dev",
            styles["contact"],
        ),
        Paragraph("PERFIL PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Desarrolladora con m\u00e1s de 2 a\u00f1os de experiencia en desarrollo "
            "de software, mantenimiento de aplicaciones e <b>integraci\u00f3n de "
            "sistemas</b> mediante <b>APIs REST</b> (JSON). Dominio de <b>C#</b>, "
            "<b>.NET</b>, <b>JavaScript</b>, <b>TypeScript</b>, <b>HTML</b>, "
            "<b>Python</b> y <b>SQL</b> (<b>SQL Server</b>). Experiencia en "
            "testing/debugging, manejo de excepciones, Git, <b>GitHub</b>, "
            "<b>Azure DevOps</b>, CI/CD y metodolog\u00edas \u00e1giles "
            "(<b>Scrum</b> / Kanban). Uso de <b>Jira</b> y documentaci\u00f3n "
            "t\u00e9cnica. Inter\u00e9s en automatizaci\u00f3n, transformaci\u00f3n "
            "digital e integraciones ERP/CRM. Disponible para modalidad "
            "<b>presencial en Guayaquil</b>.",
            styles["body"],
        ),
        Paragraph("EXPERIENCIA PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer",
            styles["job_title"],
        ),
        Paragraph("Octubre 2023 - Presente | Remoto (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Desarrollo y mantenimiento de software corporativo con <b>C#</b>, "
        "<b>.NET</b>, <b>JavaScript</b>, <b>TypeScript</b> y Node.js.",
        "Integraci\u00f3n de sistemas mediante <b>APIs REST</b> (JSON); "
        "consultas y cambios en <b>SQL Server</b> y PostgreSQL.",
        "Debugging, testing funcional, manejo de excepciones y seguimiento "
        "de logs/incidencias en prueba y producci\u00f3n.",
        "Versionamiento con <b>Git</b> / Azure Repos; pipelines <b>CI/CD</b> "
        "en <b>Azure DevOps</b>; trabajo \u00e1gil (Scrum) con <b>Jira</b>.",
        "Documentaci\u00f3n t\u00e9cnica; colaboraci\u00f3n en proyectos de "
        "evoluci\u00f3n digital en entorno fintech (Diners Club).",
        "Automatizaci\u00f3n de tareas con scripts (Bash/Python) para "
        "optimizar procesos operativos.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo web con <b>HTML</b>, JavaScript, TypeScript y Angular; "
        "integraci\u00f3n con APIs.",
        "Mantenimiento correctivo; gesti\u00f3n de tareas con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "C# / .NET 8, Angular, microservicios, APIs REST, SQL",
            [
                "Plataforma full stack con integraciones API y arquitectura "
                "por servicios.",
            ],
        ),
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "Python, Django/DRF, PostgreSQL, JWT, APIs REST",
            [
                "API con reglas de negocio, autenticaci\u00f3n y "
                "documentaci\u00f3n t\u00e9cnica.",
            ],
        ),
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "JavaScript, TypeScript, React, HTML/CSS, REST",
            [
                "Interfaces web con integraci\u00f3n backend y autenticaci\u00f3n JWT.",
            ],
        ),
    ]
    for title, meta, items in projects:
        story.append(Paragraph(title, styles["job_title"]))
        story.append(Paragraph(meta, styles["job_meta"]))
        for item in items:
            story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("HABILIDADES T\u00c9CNICAS", styles["section"]))
    story.append(section_rule())
    skills = [
        (
            "Lenguajes:",
            "C#, .NET, JavaScript, TypeScript, HTML, Python; "
            "VB.NET / Java / Spring Boot (aprendizaje / base transferible)",
        ),
        (
            "APIs / datos:",
            "REST, JSON; SQL Server, PostgreSQL; Oracle / SOAP / XML "
            "(conocimiento en progreso)",
        ),
        (
            "Calidad:",
            "Debugging, testing funcional, excepciones, logs; "
            "Jest / JUnit (b\u00e1sico / aprendizaje)",
        ),
        (
            "DevOps / cloud:",
            "Git, GitHub, Azure DevOps, CI/CD; contenedores / IaC "
            "(b\u00e1sico); seguridad en desarrollo (buenas pr\u00e1cticas)",
        ),
        (
            "Plus:",
            "Jira, documentaci\u00f3n t\u00e9cnica, Scrum/Kanban; "
            "Power BI / SharePoint / ERP-CRM-BPM (inter\u00e9s)",
        ),
    ]
    for label, value in skills:
        story.append(Paragraph("<b>" + label + "</b> " + value, styles["skill"]))

    story.append(Paragraph("EDUCACI\u00d3N", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "Tecnolog\u00eda en Desarrollo de Software - Universidad UTE",
            styles["body"],
        )
    )
    story.append(
        Paragraph("Ingenier\u00eda en Mecatr\u00f3nica - Universidad UTE", styles["body"])
    )

    story.append(Paragraph("IDIOMAS", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "<b>Espa\u00f1ol:</b> Nativo &nbsp;|&nbsp; <b>Ingl\u00e9s:</b> Intermedio",
            styles["body"],
        )
    )
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "<i>GitHub: https://github.com/Witch19 | Referencias disponibles a solicitud</i>",
        styles["body"],
    ))

    doc.build(story)
    print("CV generado: " + OUTPUT)


if __name__ == "__main__":
    main()
