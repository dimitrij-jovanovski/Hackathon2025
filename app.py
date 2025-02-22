from apscheduler.triggers.date import DateTrigger
from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from repositories.SrekjaRepository import SrekjaRepository
from services.ChatBotService import ChatBotService
from services.FillDataBase import FillDataBase
from routes.routes import opel_routes  # Ensure this exists and is correct
from datetime import datetime

# Initialize Flask App
app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(opel_routes)

# Initialize Scheduler
scheduler = BackgroundScheduler(daemon=True)

# Schedule tasks
scheduler.add_job(SrekjaRepository.initialize_database)

#scheduler.add_job(FillDataBase.populate_database, trigger=DateTrigger(run_date=datetime.now()))

#scheduler.add_job(
#    TechnicalAnalysis.init,
#    IntervalTrigger(hours=24),
#    next_run_time=datetime.now()
#)
scheduler.start()

# Run the app
if __name__ == "__main__":
    app.run()
