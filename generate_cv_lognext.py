# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra Full Stack CV for Lognext IA role."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/Joselyn_Saavedra_CV_Lognext_FullStack_IA.pdf"

ACCENT = colors.HexColor("#0066A1")
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
            "Full-Stack Developer | Node.js | React | IA Aplicada | Azure DevOps",
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
            "entornos corporativos, construyendo y evolucionando aplicaciones web "
            "backend y frontend. Dominio de <b>Node.js</b>, <b>JavaScript</b>, "
            "<b>TypeScript</b>, <b>Python</b>, <b>.NET</b>, <b>React</b> y "
            "<b>Angular</b>. Experiencia con <b>APIs REST</b>, bases <b>SQL/NoSQL</b>, "
            "<b>Git</b>, <b>Azure DevOps</b> y <b>CI/CD</b>. Uso diario de "
            "<b>IA generativa</b> (Cursor, ChatGPT, Claude, GitHub Copilot) para "
            "acelerar desarrollo, debugging y documentaci\u00f3n. Capacidad para "
            "trabajar sobre c\u00f3digo existente, resolver incidencias, automatizar "
            "procesos y colaborar con equipos t\u00e9cnicos y funcionales. "
            "Motivaci\u00f3n por chatbots, integraciones cloud e IA aplicada.",
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
        "Desarrollo y mantenimiento evolutivo de aplicaciones corporativas "
        "(backend + frontend) con <b>Node.js</b>, <b>TypeScript</b>, <b>JavaScript</b> y <b>.NET</b>.",
        "Integraci\u00f3n de <b>APIs REST</b> y servicios externos; consultas y cambios en "
        "bases <b>SQL Server</b>, <b>PostgreSQL</b> y <b>MongoDB</b>.",
        "Trabajo sobre c\u00f3digo existente: debugging, resoluci\u00f3n de incidencias y "
        "mejora de funcionalidades en prueba y producci\u00f3n.",
        "Control de versiones con <b>Git</b>, Azure Repos y pipelines <b>CI/CD</b> en <b>Azure DevOps</b>.",
        "Automatizaci\u00f3n de tareas con scripts Bash; documentaci\u00f3n t\u00e9cnica de soluciones.",
        "Uso de <b>IA generativa</b> en el flujo de desarrollo para optimizar productividad y calidad.",
        "Colaboraci\u00f3n remota con equipos t\u00e9cnicos y funcionales en entorno fintech (Diners Club).",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo web con <b>Angular</b>, HTML, JavaScript y TypeScript; integraci\u00f3n con APIs.",
        "Mantenimiento correctivo de interfaces; trabajo \u00e1gil con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Pet Adoption UI - github.com/Witch19/pet-adoption-ui",
            "React, TypeScript, Tailwind, REST APIs, JWT",
            ["Frontend moderno con integraci\u00f3n backend y flujos conversacionales de UI."],
        ),
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "Python, Django, DRF, PostgreSQL, JWT",
            ["API REST corporativa con autenticaci\u00f3n, reglas de negocio y documentaci\u00f3n."],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            ".NET 8, Angular, microservicios, APIs REST",
            ["Plataforma full stack con integraciones API y arquitectura escalable."],
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
        ("Full-Stack:", "Node.js, NestJS, Python, .NET, JavaScript, TypeScript, React, Angular, HTML/CSS"),
        ("Datos:", "PostgreSQL, SQL Server, MongoDB, SQL / NoSQL"),
        ("Cloud / DevOps:", "Azure DevOps, Azure Repos, CI/CD, Git, GitFlow (buenas pr\u00e1cticas)"),
        ("IA aplicada:", "Cursor, ChatGPT, Claude, GitHub Copilot; inter\u00e9s en LLMs, RAG, automatizaci\u00f3n"),
        ("Valorables:", "Chatbots / Bot Framework (inter\u00e9s y aprendizaje); Azure Functions (b\u00e1sico)"),
        ("Soft skills:", "An\u00e1lisis t\u00e9cnico, resoluci\u00f3n de incidencias, trabajo en equipo, adaptabilidad"),
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
