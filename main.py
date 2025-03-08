import logging

# Configure logging with basic settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('bot.log')
    ]
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        logger.info("Starting bot...")
        from app import app
        
        # Start the Flask application
        app.run(host='0.0.0.0', port=54321, debug=False)
        
    except Exception as e:
        logger.error(f"Bot crashed: {str(e)}", exc_info=True) 