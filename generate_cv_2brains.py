# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra Full Stack CV for 2Brains / Codelco project."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_2Brains_FullStack.pdf"

ACCENT = colors.HexColor("#1B3A4B")
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
            "Full Stack Developer | Node.js | NestJS | React | TypeScript | Azure DevOps",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Remoto (experiencia Chile) | github.com/Witch19",
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
            "Desarrolladora Full Stack con m\u00e1s de 2 a\u00f1os de experiencia "
            "en aplicaciones web productivas, integraciones y trabajo con equipos "
            "multidisciplinarios (remoto Ecuador/Chile). Dominio de <b>Node.js</b>, "
            "<b>NestJS</b>, <b>TypeScript</b>, <b>React</b> y APIs REST. Experiencia "
            "en bases de datos, reglas de negocio, <b>Git</b>, code reviews, "
            "metodolog\u00edas \u00e1giles (Scrum) y pipelines <b>CI/CD</b> en "
            "<b>Azure DevOps</b>. Capacidad para levantar requerimientos, documentar "
            "y colaborar con perfiles t\u00e9cnicos y de negocio. Inter\u00e9s en "
            "visualizaci\u00f3n de datos, OAuth 2.0 y proyectos industriales de "
            "alto impacto. Sin experiencia en miner\u00eda; motivaci\u00f3n por "
            "aprender el dominio del proyecto.",
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
        "Dise\u00f1o, desarrollo e integraci\u00f3n de aplicaciones web "
        "productivas (frontend + backend) con <b>Node.js</b>, <b>TypeScript</b>, "
        "<b>React</b> y <b>.NET</b>.",
        "Construcci\u00f3n y mantenimiento de <b>APIs REST</b>; aplicaci\u00f3n "
        "de reglas de negocio e integraci\u00f3n de fuentes de datos "
        "(<b>SQL Server</b>, PostgreSQL, MongoDB).",
        "Interfaces responsivas con <b>React</b> / Angular; foco en claridad "
        "de UI y experiencia de usuario.",
        "Versionamiento en <b>Git</b> corporativo (Azure Repos); participaci\u00f3n "
        "en flujos CI/CD y buenas pr\u00e1cticas de desarrollo.",
        "Debugging, pruebas funcionales/regresi\u00f3n en prueba y producci\u00f3n; "
        "documentaci\u00f3n t\u00e9cnica y transfer de conocimiento.",
        "Trabajo \u00e1gil (Scrum/sprints) con equipos t\u00e9cnicos y funcionales "
        "en entorno corporativo regulado (fintech / Diners Club).",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo frontend con Angular, TypeScript y JavaScript; "
        "integraci\u00f3n con APIs.",
        "Mantenimiento de interfaces; trabajo \u00e1gil con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "React, TypeScript, Tailwind, REST APIs, JWT",
            [
                "Interfaces React/TypeScript con autenticaci\u00f3n e "
                "integraci\u00f3n backend.",
            ],
        ),
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "APIs REST, PostgreSQL, JWT, reglas de negocio",
            [
                "API documentada con autenticaci\u00f3n, modelado de datos "
                "y l\u00f3gica de negocio.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            ".NET 8, Angular, microservicios, APIs REST",
            [
                "Plataforma full stack con integraciones y arquitectura "
                "por servicios.",
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
            "Back End:",
            "Node.js, NestJS, TypeScript, APIs REST, reglas de negocio, "
            "integraci\u00f3n de datos",
        ),
        (
            "Front End:",
            "React.js, TypeScript, Angular, UI responsiva; "
            "Next.js / Plotly / Nivo / Leaflet (aprendizaje activo)",
        ),
        (
            "Datos:",
            "SQL Server, PostgreSQL, MongoDB; consultas y modelado",
        ),
        (
            "Calidad / Git:",
            "Git, code reviews, CI/CD, pruebas funcionales y de regresi\u00f3n; "
            "unitarias (b\u00e1sico)",
        ),
        (
            "Cloud / seguridad:",
            "Azure DevOps, CI/CD; OAuth 2.0 / JWT (pr\u00e1ctica); "
            "Kubernetes / APIM / OWASP (conocimiento en progreso)",
        ),
        (
            "Colaboraci\u00f3n:",
            "Scrum, historias de usuario, documentaci\u00f3n, trabajo "
            "multidisciplinario",
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
