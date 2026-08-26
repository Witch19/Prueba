# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra CV for elrow / Monegros Front-End freelance."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_elrow_Frontend.pdf"

ACCENT = colors.HexColor("#C2185B")
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
            "Front-End Developer Freelance | React | Tailwind CSS | TypeScript | UI/UX",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Remoto freelance (horario flexible) | github.com/Witch19",
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
            "Desarrolladora front-end freelance con m\u00e1s de 2 a\u00f1os de "
            "experiencia en <b>React</b>, <b>TypeScript</b> y <b>Tailwind CSS</b>, "
            "creando interfaces modernas, responsive y con ojo para el dise\u00f1o. "
            "C\u00f3digo limpio, reutilizable y mantenible. Experiencia depurando "
            "y evolucionando aplicaciones existentes, integrando APIs y trabajando "
            "con autonom\u00eda en remoto (as\u00edncrono). Fluidez con <b>Git</b> "
            "y flujos de equipo. Familiaridad con entornos full stack; "
            "disponibilidad para colaborar en stacks con Laravel / InertiaJS "
            "aprendiendo el contexto del proyecto con rapidez. Motivada por "
            "marcas creativas y experiencias visuales de alto impacto.",
            styles["body"],
        ),
        Paragraph("EXPERIENCIA PROFESIONAL", styles["section"]),
        section_rule(),
        Paragraph(
            "Vidortec / Vigatec Chile - Full-Stack Developer (enfoque Front-End)",
            styles["job_title"],
        ),
        Paragraph("Octubre 2023 - Presente | Remoto freelance-compatible", styles["job_meta"]),
    ]

    for item in [
        "Desarrollo de UI con <b>React</b>, <b>TypeScript</b> y Angular; "
        "componentes reutilizables y dise\u00f1os responsive.",
        "Mejora de UI/UX, depuraci\u00f3n y soporte a c\u00f3digo existente "
        "en aplicaciones web productivas.",
        "Integraci\u00f3n con APIs REST; colaboraci\u00f3n t\u00e9cnica "
        "as\u00edncrona con equipos remotos.",
        "Git, code reviews y entregas con plazos; autonom\u00eda e iniciativa.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Interfaces web con TypeScript/JavaScript; mantenimiento correctivo "
        "y trabajo \u00e1gil.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PORTFOLIO / PROYECTOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Pet Adoption UI - github.com/Witch19/pet-adoption-ui",
            "React + TypeScript + Tailwind CSS + REST + JWT",
            [
                "UI moderna y responsive con Tailwind; componentes limpios "
                "e integraci\u00f3n API.",
            ],
        ),
        (
            "Billing UI - github.com/Witch19/billing-ui",
            "React + TypeScript + Tailwind CSS",
            [
                "Formularios y flujos de UI con foco en usabilidad, "
                "estados y c\u00f3digo mantenible.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            "Frontend TypeScript (Angular) + APIs",
            [
                "Experiencia full stack demostrando UI de producto "
                "e integraciones.",
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
            "Core:",
            "React, Tailwind CSS, TypeScript, JavaScript, HTML/CSS, "
            "UI responsive, componentes reutilizables",
        ),
        (
            "Colaboraci\u00f3n:",
            "Git, trabajo en equipo remoto, comunicaci\u00f3n as\u00edncrona "
            "(Teams/similares), autonom\u00eda",
        ),
        (
            "Entorno del rol:",
            "Laravel + InertiaJS (aprendizaje activo / colaboraci\u00f3n "
            "en codebase existente)",
        ),
        (
            "Soft:",
            "Ojo para el dise\u00f1o, iniciativa, plazos ajustados, "
            "depuraci\u00f3n y soporte",
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
        "<i>Portfolio GitHub: https://github.com/Witch19 | "
        "Tarifa freelance: disponible a solicitud / ver email de postulaci\u00f3n</i>",
        styles["body"],
    ))

    doc.build(story)
    print("CV generado: " + OUTPUT)


if __name__ == "__main__":
    main()
