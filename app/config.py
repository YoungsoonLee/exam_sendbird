import os

# DATABASE URL & SETTING
DATABASE = {
    'engine': os.getenv('DB_ENGINE') or 'postgres',
    'host': os.getenv('DB_HOST') or 'elmer.db.elephantsql.com',
    'port': os.getenv('DB_PORT') or '5432',
    'user': os.getenv('DB_USER') or 'sgglztrm',
    'password': os.getenv('DB_PASSWORD') or 'oKz6_lsbABDHMJ80HjRhVjsxpggfAcQE',
    'database': os.getenv('DB_DATABASE') or 'sgglztrm'
}

DATABASE_URI = '%(engine)s://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s' % DATABASE