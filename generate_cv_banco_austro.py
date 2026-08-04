# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for Banco del Austro - Analista de Desarrollo TI."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_Banco_Austro.pdf"

ACCENT = colors.HexColor("#003366")
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
            "Analista de Desarrollo TI | C# / .NET | Angular | React | SQL | Banca",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Disponible Guayaquil / Remoto | github.com/Witch19",
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
            "Analista / Desarrolladora Full-Stack con m\u00e1s de 2 a\u00f1os de experiencia "
            "en entornos <b>bancarios y fintech</b>, participando en el desarrollo, "
            "mantenimiento e <b>integraci\u00f3n de plataformas financieras</b>. Dominio de "
            "<b>C#</b>, <b>.NET</b>, <b>Angular</b>, <b>React</b>, <b>JavaScript</b> y "
            "<b>SQL</b>. Experiencia con control de versiones (<b>Git</b>), metodolog\u00edas "
            "\u00e1giles y trabajo colaborativo con equipos t\u00e9cnicos y de negocio. "
            "Formaci\u00f3n en Desarrollo de Software. Orientada a calidad, resoluci\u00f3n "
            "de incidencias y evoluci\u00f3n de sistemas existentes.",
            styles["body"],
        ),
        Paragraph("EXPERIENCIA PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer (entorno bancario)",
            styles["job_title"],
        ),
        Paragraph("Octubre 2023 - Presente | Remoto (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Desarrollo y mantenimiento de aplicaciones en entorno <b>fintech / bancario</b> "
        "(proyecto <b>Diners Club</b>): tarjetas, gesti\u00f3n de perfiles y plataformas internas.",
        "Programaci\u00f3n backend con <b>C#</b> / <b>.NET</b> y Node.js; frontend con "
        "<b>Angular</b>, <b>React</b> y <b>JavaScript/TypeScript</b>.",
        "Integraci\u00f3n de servicios y plataformas financieras mediante <b>APIs REST</b>; "
        "consultas y cambios en bases <b>SQL Server</b> y PostgreSQL.",
        "Control de versiones con <b>Git</b> (Azure Repos) y trabajo bajo metodolog\u00edas "
        "\u00e1giles (sprints, Jira / Azure DevOps).",
        "An\u00e1lisis t\u00e9cnico, debugging y resoluci\u00f3n de incidencias en prueba y producci\u00f3n.",
        "Colaboraci\u00f3n con equipos funcionales para convertir necesidades de negocio "
        "en soluciones tecnol\u00f3gicas.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo web con <b>Angular</b>, HTML, <b>JavaScript</b> y TypeScript; "
        "integraci\u00f3n con APIs.",
        "Mantenimiento correctivo de interfaces; trabajo \u00e1gil con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "C# / .NET 8, Angular, microservicios, APIs REST, SQL",
            [
                "Plataforma full stack con backend .NET, frontend Angular e "
                "integraciones API.",
            ],
        ),
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "React, TypeScript, JavaScript, REST APIs, JWT",
            [
                "Interfaces modernas con React e integraci\u00f3n a servicios backend.",
            ],
        ),
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "APIs REST, PostgreSQL (SQL), autenticaci\u00f3n JWT",
            [
                "API con reglas de negocio, modelos de datos SQL y documentaci\u00f3n.",
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
        ("Stack solicitado:", "C#, .NET, Angular, React, JavaScript, SQL"),
        ("Backend adicional:", "Node.js, TypeScript, Python, APIs REST"),
        ("Bases de datos:", "SQL Server, PostgreSQL, MongoDB"),
        ("Herramientas:", "Git, Azure DevOps, Jira, CI/CD, metodolog\u00edas \u00e1giles"),
        (
            "Dominio banca:",
            "Integraci\u00f3n de plataformas financieras, sistemas de tarjetas, "
            "entorno corporativo regulado",
        ),
        (
            "Soft skills:",
            "An\u00e1lisis t\u00e9cnico, resoluci\u00f3n de incidencias, trabajo en equipo, "
            "comunicaci\u00f3n con negocio",
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
