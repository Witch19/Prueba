# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for CRESA Desarrollador Web Junior."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_CRESA_Web_Junior.pdf"

ACCENT = colors.HexColor("#0B4F6C")
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
            "Desarrolladora Web Junior | HTML | CSS | JavaScript | SQL Server | Soporte de Aplicaciones",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Disponible Guayaquil | github.com/Witch19",
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
            "Desarrolladora web con m\u00e1s de 2 a\u00f1os de experiencia en "
            "desarrollo y <b>mantenimiento de plataformas web</b> y aplicaciones "
            "en producci\u00f3n. Dominio de <b>HTML</b>, <b>CSS</b> y "
            "<b>JavaScript</b>, con experiencia en soporte de aplicaciones, "
            "resoluci\u00f3n de incidencias y mejora de la experiencia de usuario. "
            "Manejo de bases de datos relacionales (<b>SQL Server</b>, "
            "PostgreSQL / MySQL). Proactiva, organizada y con alta disposici\u00f3n "
            "para aprender nuevas herramientas. Colaboraci\u00f3n habitual con "
            "equipos t\u00e9cnicos y de negocio. Disponible para incorporaci\u00f3n "
            "en <b>Guayaquil</b>.",
            styles["body"],
        ),
        Paragraph("EXPERIENCIA PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Desarrolladora Full-Stack / Soporte de aplicaciones",
            styles["job_title"],
        ),
        Paragraph("Octubre 2023 - Presente | Remoto (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Desarrollo y <b>mantenimiento de plataformas web</b> corporativas; "
        "aseguramiento de funcionalidad y experiencia de usuario.",
        "Programaci\u00f3n web con <b>HTML</b>, <b>CSS</b>, <b>JavaScript</b> "
        "y TypeScript (React / Angular); integraci\u00f3n con APIs.",
        "<b>Soporte de aplicaciones</b> en prueba y producci\u00f3n: debugging, "
        "an\u00e1lisis de incidencias y correcciones correctivas/evolutivas.",
        "Consultas y cambios en bases relacionales (<b>SQL Server</b>, "
        "PostgreSQL); apoyo a procesos operativos de sistemas.",
        "Colaboraci\u00f3n con equipos t\u00e9cnicos y funcionales; documentaci\u00f3n "
        "y organizaci\u00f3n de tareas con Git y metodolog\u00edas \u00e1giles.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo de interfaces web con <b>HTML</b>, <b>CSS</b>, "
        "<b>JavaScript</b> y Angular; mantenimiento correctivo de UI.",
        "Trabajo \u00e1gil con Jira; adaptaci\u00f3n r\u00e1pida a herramientas "
        "y metodolog\u00edas del equipo.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "HTML, CSS, JavaScript, React, TypeScript",
            [
                "Interfaces web responsivas con foco en usabilidad e "
                "integraci\u00f3n con APIs.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "Angular, JavaScript/TypeScript, APIs, SQL",
            [
                "Plataforma web tipo eCommerce: cat\u00e1logo, flujos de UI "
                "y consumo de servicios backend.",
            ],
        ),
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "APIs, PostgreSQL (SQL), autenticaci\u00f3n",
            [
                "Soporte a aplicaci\u00f3n web con modelo de datos relacional "
                "y reglas de negocio.",
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
        ("Web:", "HTML5, CSS3, JavaScript, TypeScript, React, Angular"),
        (
            "Bases de datos:",
            "SQL Server, MySQL / PostgreSQL (SQL relacional), consultas y soporte",
        ),
        (
            "Soporte / operaciones:",
            "Soporte de aplicaciones, resoluci\u00f3n de incidencias, "
            "mantenimiento de plataformas web",
        ),
        ("Herramientas:", "Git, Jira, Azure DevOps, documentaci\u00f3n t\u00e9cnica"),
        (
            "Soft skills:",
            "Proactividad, organizaci\u00f3n, aprendizaje r\u00e1pido, "
            "trabajo multidisciplinario",
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
