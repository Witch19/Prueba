# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra Full Stack CV for Signlab Laravel/Vue role."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_Signlab_Fullstack.pdf"

ACCENT = colors.HexColor("#0D7377")
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
            "Full-Stack Developer | APIs REST | SQL/NoSQL | JavaScript "
            "(inter\u00e9s Laravel / Vue)",
            styles["title"],
        ),
        Paragraph("Quito, Ecuador | Remoto | github.com/Witch19", styles["contact"]),
        Paragraph(
            "+593 99 252 3644 &nbsp;|&nbsp; Josytst.js@gmail.com &nbsp;|&nbsp; "
            "linkedin.com/in/joselyn-saavedra-dev",
            styles["contact"],
        ),
        Paragraph("PERFIL PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Desarrolladora Full-Stack con m\u00e1s de 2 a\u00f1os de experiencia en "
            "aplicaciones web a medida (SaaS, portales y plataformas internas). "
            "Stack principal: <b>Node.js</b>, <b>JavaScript/TypeScript</b>, "
            "<b>Python</b>, <b>.NET</b>, <b>React</b> y <b>Angular</b>. Experiencia "
            "s\u00f3lida en <b>APIs REST</b>, dise\u00f1o de modelos de datos "
            "<b>SQL/NoSQL</b>, an\u00e1lisis de requisitos y evoluci\u00f3n de "
            "c\u00f3digo existente. Trabajo habitual con <b>Git</b>, <b>Jira</b> y "
            "<b>Azure DevOps</b>. Aut\u00f3noma, con iniciativa y buena comunicaci\u00f3n "
            "en equipo. Inter\u00e9s activo en profundizar en <b>Laravel (PHP)</b> y "
            "<b>Vue.js</b> para aportar en proyectos full stack con ese stack.",
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
        "Desarrollo full stack de aplicaciones web corporativas (backend + frontend) "
        "con <b>Node.js</b>, <b>TypeScript</b>, <b>JavaScript</b> y <b>.NET</b>.",
        "An\u00e1lisis de flujos de negocio, definici\u00f3n de funcionalidades e "
        "integraci\u00f3n de <b>APIs REST</b> con servicios externos.",
        "Dise\u00f1o y consulta de modelos de datos en <b>SQL Server</b>, "
        "<b>PostgreSQL</b> y <b>MongoDB</b> (SQL / NoSQL).",
        "Trabajo sobre c\u00f3digo existente: debugging, resoluci\u00f3n de incidencias "
        "y mejora de legibilidad y buenas pr\u00e1cticas.",
        "Control de versiones con <b>Git</b>; gesti\u00f3n de tareas y colaboraci\u00f3n "
        "con <b>Jira</b> / Azure DevOps y pipelines CI/CD.",
        "Documentaci\u00f3n t\u00e9cnica y estimaci\u00f3n de tareas en entorno remoto "
        "con equipos t\u00e9cnicos y funcionales (fintech / Diners Club).",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo web con <b>Angular</b>, HTML, JavaScript y TypeScript; "
        "integraci\u00f3n con APIs REST.",
        "Mantenimiento de interfaces y trabajo \u00e1gil con <b>Jira</b>.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "Python, Django, DRF, PostgreSQL, JWT",
            [
                "API REST con autenticaci\u00f3n, reglas de negocio, modelos de datos "
                "y documentaci\u00f3n t\u00e9cnica.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            ".NET 8, Angular, microservicios, APIs REST",
            [
                "Plataforma full stack con integraciones API y arquitectura por "
                "servicios.",
            ],
        ),
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "React, TypeScript, Tailwind, REST APIs, JWT",
            [
                "Frontends modernos con integraci\u00f3n backend, autenticaci\u00f3n y "
                "flujos de UI.",
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
            "Backend:",
            "Node.js, NestJS, Python, .NET, JavaScript, TypeScript; "
            "Laravel / PHP (aprendizaje activo)",
        ),
        (
            "Frontend:",
            "React, Angular, HTML/CSS, JavaScript/TypeScript; "
            "Vue.js (aprendizaje activo)",
        ),
        ("Datos:", "PostgreSQL, SQL Server, MongoDB, dise\u00f1o de modelos SQL / NoSQL"),
        ("APIs / pr\u00e1cticas:", "REST APIs, c\u00f3digo legible, buenas pr\u00e1cticas, debugging"),
        ("Herramientas:", "Git, Jira, Azure DevOps, CI/CD, Trello (familiar)"),
        (
            "Soft skills:",
            "An\u00e1lisis de requisitos, autonom\u00eda, iniciativa, comunicaci\u00f3n, "
            "aprendizaje continuo",
        ),
    ]
    for label, value in skills:
        story.append(Paragraph("<b>" + label + "</b> " + value, styles["skill"]))

    story.append(Paragraph("EDUCACI\u00d3N", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph("Tecnolog\u00eda en Desarrollo de Software - Universidad UTE", styles["body"])
    )
    story.append(Paragraph("Ingenier\u00eda en Mecatr\u00f3nica - Universidad UTE", styles["body"]))

    story.append(Paragraph("IDIOMAS", styles["section"]))
    story.append(section_rule())
    story.append(
        Paragraph("<b>Espa\u00f1ol:</b> Nativo &nbsp;|&nbsp; <b>Ingl\u00e9s:</b> Intermedio", styles["body"])
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
