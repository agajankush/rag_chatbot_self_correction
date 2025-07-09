import psycopg2
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
print(os.getenv('DB_PORT'))

def get_db_connection():
    """Establish a connection to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def initialize_database():
    """Initialize the database by creating the necessary tables."""
    connection = get_db_connection()
    if connection is None:
        return

    if connection:
        try:
            cursor = connection.cursor()
            
            #1. Enable the pgvecotr extension
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            print("pgvector extension enabled.")
            
            #2. Create the document_chunks table
            # vector(1536) specifies a vector dimension of 1536 for OpenAI's text-embedding-3-small
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS document_chunks (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    embedding VECTOR(1536) NOT NULL,
                    source TEXT,
                    metadata JSONB
                );
                
            """)
            connection.commit()
            print("Table 'document_chunks' created successfully.")
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing the database: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database. Initialization aborted.")

if __name__ == "__main__":
    initialize_database()
    