# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra Frontend CV for Lumation."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_Lumation_Frontend.pdf"

ACCENT = colors.HexColor("#1A6B5A")
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
            "Frontend Developer | JavaScript | TypeScript | Angular | React | Node.js",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Remoto / h\u00edbrido flexible | github.com/Witch19",
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
            "Frontend Developer con m\u00e1s de 2 a\u00f1os de experiencia construyendo "
            "interfaces web con <b>JavaScript</b> y <b>TypeScript</b>, usando "
            "<b>Angular</b> y <b>React</b>. Dominio de <b>HTML/CSS</b>, layouts "
            "responsivos con <b>Flexbox</b> y <b>CSS Grid</b>, y buenas pr\u00e1cticas "
            "b\u00e1sicas de accesibilidad web. Experiencia integrando UIs con "
            "<b>APIs REST</b> y <b>Node.js</b>. Trabajo remoto en entornos corporativos, "
            "con Git, metodolog\u00edas \u00e1giles y foco en calidad de interfaz y "
            "experiencia de usuario.",
            styles["body"],
        ),
        Paragraph("EXPERIENCIA PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer (enfoque Frontend)",
            styles["job_title"],
        ),
        Paragraph("Octubre 2023 - Presente | Remoto (Ecuador / Chile)", styles["job_meta"]),
    ]

    for item in [
        "Desarrollo de interfaces con <b>Angular</b>, <b>React</b>, "
        "<b>JavaScript</b> y <b>TypeScript</b> en aplicaciones corporativas.",
        "Implementaci\u00f3n de layouts responsivos con <b>HTML/CSS</b>, "
        "<b>Flexbox</b> y <b>CSS Grid</b>; mantenimiento evolutivo de UI.",
        "Integraci\u00f3n frontend con <b>APIs REST</b> y servicios backend "
        "(<b>Node.js</b> / .NET).",
        "Control de versiones con <b>Git</b>; trabajo \u00e1gil con Jira / Azure DevOps.",
        "Debugging de interfaces, resoluci\u00f3n de incidencias y mejora de "
        "usabilidad en prueba y producci\u00f3n.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo web con <b>Angular</b>, HTML, CSS, JavaScript y TypeScript.",
        "Integraci\u00f3n con APIs; mantenimiento correctivo de interfaces; "
        "trabajo \u00e1gil con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Pet Adoption UI - github.com/Witch19/pet-adoption-ui",
            "React, TypeScript, Tailwind, REST APIs, JWT",
            [
                "UI moderna con componentes React, estilos utilitarios y "
                "dise\u00f1o responsivo.",
            ],
        ),
        (
            "Billing UI - github.com/Witch19/billing-ui",
            "React, TypeScript, Tailwind, APIs",
            [
                "Frontend de facturaci\u00f3n con formularios, estados de UI e "
                "integraci\u00f3n backend.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "Angular, TypeScript, .NET 8, APIs REST",
            [
                "Frontend Angular en plataforma eCommerce con consumo de APIs.",
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
        ("Lenguajes:", "JavaScript (avanzado), TypeScript (avanzado)"),
        ("Frameworks:", "Angular 8+, React"),
        (
            "UI / CSS:",
            "HTML5, CSS3, Flexbox, CSS Grid, dise\u00f1o responsivo, "
            "accesibilidad web b\u00e1sica (a11y)",
        ),
        ("Backend relacionado:", "Node.js, APIs REST, autenticaci\u00f3n JWT"),
        ("Herramientas:", "Git, Azure DevOps, Jira, Tailwind CSS"),
        (
            "Soft skills:",
            "Trabajo en equipo, comunicaci\u00f3n, aprendizaje continuo, "
            "resoluci\u00f3n de incidencias de UI",
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
