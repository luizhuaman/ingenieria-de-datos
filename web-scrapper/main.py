import argparse  #  Libreria estandar para análisis de opciones y argumentos de línea de comando
import logging  # Libreria estandar para informe de estado, error y mensajes informativos
logging.basicConfig(level=logging.INFO)

from common import config


logger = logging.getLogger(__name__)


def _news_scraper(news_site):
    host = config()['news_sites'][news_site]['url']

    logging.info('Beginning scraper for {}'.format(host))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Parseador de argumentos

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site', 
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)
    
    args = parser.parse_args()
    _news_scraper(args.news_site)