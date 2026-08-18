# -*- coding: utf-8 -*-
"""Generate Joselyn Saavedra Full Stack CV for Construex."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer

OUTPUT = "/workspace/cv/Joselyn_Saavedra_CV_Construex_FullStack.pdf"

ACCENT = colors.HexColor("#E85D04")
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
            "Full Stack Developer | TypeScript | Python | React | NestJS | PostgreSQL",
            styles["title"],
        ),
        Paragraph(
            "Quito, Ecuador | Presencial / H\u00edbrida | github.com/Witch19",
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
            "Desarrolladora Full Stack con m\u00e1s de 2 a\u00f1os de experiencia en "
            "aplicaciones web en producci\u00f3n, gestionando el ciclo completo "
            "frontend y backend. Dominio de <b>TypeScript</b>, <b>React</b>, "
            "<b>Node.js</b>, <b>NestJS</b> y <b>Python</b> (Django/DRF). "
            "Experiencia en dise\u00f1o y optimizaci\u00f3n de consultas en "
            "<b>PostgreSQL</b>, <b>SQL Server</b> y <b>MongoDB</b>. "
            "Trabajo con <b>Git</b>, metodolog\u00edas \u00e1giles (Scrum), "
            "code reviews y buenas pr\u00e1cticas (Clean Code). Aut\u00f3noma, "
            "orientada a resolver problemas complejos y construir soluciones "
            "escalables. Resido en <b>Quito</b>. Inter\u00e9s en plataformas "
            "SaaS y productos de alto impacto regional.",
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
        "Desarrollo full stack de aplicaciones web en producci\u00f3n con "
        "<b>TypeScript</b>, <b>JavaScript</b>, <b>Node.js</b>, <b>React</b> y <b>.NET</b>.",
        "Implementaci\u00f3n y mantenimiento de <b>APIs REST</b>; integraci\u00f3n "
        "frontend-backend con foco en seguridad y escalabilidad.",
        "Dise\u00f1o y optimizaci\u00f3n de consultas en <b>PostgreSQL</b>, "
        "<b>SQL Server</b> y <b>MongoDB</b>; modelado de datos SQL/NoSQL.",
        "Trabajo sobre c\u00f3digo existente: debugging, resoluci\u00f3n de incidencias, "
        "mejora de legibilidad y est\u00e1ndares de calidad.",
        "Control de versiones con <b>Git</b>; pipelines CI/CD en Azure DevOps; "
        "metodolog\u00edas \u00e1giles (sprints, Jira).",
        "Colaboraci\u00f3n con equipos t\u00e9cnicos y funcionales para traducir "
        "requerimientos de negocio en soluciones robustas.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("Advance Latam - Frontend Developer", styles["job_title"]))
    story.append(Paragraph("Junio 2023 - Agosto 2023 | Ecuador", styles["job_meta"]))
    for item in [
        "Desarrollo frontend con <b>Angular</b>, TypeScript y JavaScript; "
        "integraci\u00f3n con APIs REST.",
        "Mantenimiento evolutivo de interfaces; trabajo \u00e1gil con Jira.",
    ]:
        story.append(bullet(item, styles["bullet"]))

    story.append(Paragraph("PROYECTOS DESTACADOS (GitHub)", styles["section"]))
    story.append(section_rule())

    projects = [
        (
            "Backend Urbanizaci\u00f3n - github.com/Witch19/backendUrbanizacion",
            "Python, Django, DRF, PostgreSQL, JWT, pruebas",
            [
                "API REST con autenticaci\u00f3n, reglas de negocio, modelado "
                "PostgreSQL y documentaci\u00f3n t\u00e9cnica.",
            ],
        ),
        (
            "Pet Adoption UI / Billing UI - github.com/Witch19",
            "React, TypeScript, Tailwind, REST APIs, JWT",
            [
                "Componentes reutilizables, integraci\u00f3n backend y UI "
                "responsiva con TypeScript.",
            ],
        ),
        (
            "Tienda de Frutas - github.com/Witch19/tienda_bnk",
            ".NET 8, Angular, microservicios, APIs REST, SQL",
            [
                "Plataforma full stack con arquitectura por servicios e "
                "integraciones API.",
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
            "Frontend:",
            "TypeScript, JavaScript, React, HTML/CSS, componentes reutilizables; "
            "Next.js (conocimiento y aprendizaje activo en SSR/SSG)",
        ),
        (
            "Backend:",
            "Python (Django, DRF), Node.js, NestJS, TypeScript, APIs REST, "
            "microservicios",
        ),
        (
            "Bases de datos:",
            "PostgreSQL, SQL Server, MongoDB; dise\u00f1o de esquemas y "
            "optimizaci\u00f3n de consultas",
        ),
        (
            "Pr\u00e1cticas:",
            "Git, Scrum, code reviews, Clean Code, pruebas unitarias (b\u00e1sico), CI/CD",
        ),
        (
            "Soft skills:",
            "Autonom\u00eda, proactividad, resoluci\u00f3n de problemas, "
            "comunicaci\u00f3n en equipo",
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
