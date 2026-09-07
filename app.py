from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    services = [
        {
            "title": "Software & Web Engineering",
            "desc": "Custom enterprise software, high-performance web applications, and scalable API systems.",
            "icon": "bi-code-slash",
            "tech": "Python / Flask / Microservices"
        },
        {
            "title": "AI & Algorithmic Solutions",
            "desc": "Cutting-edge AI integrations, smart process automation, and algorithmic trading systems.",
            "icon": "bi-cpu-fill",
            "tech": "Neural Networks / Algo-Trading / Automation"
        },
        {
            "title": "Digital Products & Assets",
            "desc": "Ready-to-deploy digital templates, developer frameworks, and proprietary fintech tools.",
            "icon": "bi-box-seam-fill",
            "tech": "SaaS Assets / Digital Delivery"
        },
        {
            "title": "Technical Education & Mentorship",
            "desc": "Advanced tech training, algorithmic strategy workshops, and developer skill programs.",
            "icon": "bi-journal-code",
            "tech": "Interactive Training / Mentorship"
        }
    ]

    testimonials = [
        {
            "name": "Satisfied Client 1",
            "company": "Trading Firm / Investor",
            "service": "Algorithmic Trading Architecture",
            "icon": "bi-graph-up-arrow",
            "feedback": "The custom trading algorithm developed for our strategy is exceptionally fast and precise. Highly satisfied with the AI integration and risk management features!"
        },
        {
            "name": "Satisfied Client 2",
            "company": "E-Commerce Business Partner",
            "service": "Web Software Development",
            "icon": "bi-globe",
            "feedback": "Our corporate web portal was built with outstanding performance and clean architecture. Prompt communication and high technical standards throughout the project."
        }
    ]

    return render_template('index.html', services=services, testimonials=testimonials)

if __name__ == '__main__':
    app.run(debug=True)