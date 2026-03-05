from flask import Flask, render_template
from config import Config
from routes.campaign_routes import campaign_bp
from routes.pitch_routes import pitch_bp
from routes.lead_routes import lead_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(campaign_bp)
    app.register_blueprint(pitch_bp)
    app.register_blueprint(lead_bp)

    # Dashboard route
    @app.route("/")
    def index():
        return render_template("index.html")

    # Module page routes
    @app.route("/campaign")
    def campaign_page():
        return render_template("campaign.html")

    @app.route("/pitch")
    def pitch_page():
        return render_template("pitch.html")

    @app.route("/lead-scoring")
    def lead_scoring_page():
        return render_template("lead_scoring.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5000)
