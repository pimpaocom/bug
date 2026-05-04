#!/usr/bin/env python3
"""
LinkedIn public job search for Switzerland.
Uses LinkedIn's guest API (no login required).
"""

import sys
import time
import argparse
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

GUEST_API = (
    "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
)


def fetch_jobs(keywords: str, location: str = "Switzerland", max_results: int = 25) -> list[dict]:
    jobs = []
    start = 0
    batch = 10

    while len(jobs) < max_results:
        params = {
            "keywords": keywords,
            "location": location,
            "start": start,
            "count": batch,
            "f_TP": "1,2",  # posted in past month
        }
        try:
            resp = requests.get(GUEST_API, params=params, headers=HEADERS, timeout=15)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"[erro] Falha ao ligar ao LinkedIn: {e}", file=sys.stderr)
            break

        soup = BeautifulSoup(resp.text, "lxml")
        cards = soup.find_all("li")

        if not cards:
            break

        for card in cards:
            title_el = card.find("h3", class_="base-search-card__title")
            company_el = card.find("h4", class_="base-search-card__subtitle")
            location_el = card.find("span", class_="job-search-card__location")
            date_el = card.find("time")
            link_el = card.find("a", class_="base-card__full-link")

            if not title_el:
                continue

            jobs.append({
                "titulo": title_el.get_text(strip=True),
                "empresa": company_el.get_text(strip=True) if company_el else "—",
                "localização": location_el.get_text(strip=True) if location_el else "—",
                "data": date_el.get("datetime", "—") if date_el else "—",
                "link": link_el["href"].split("?")[0] if link_el else "—",
            })

            if len(jobs) >= max_results:
                break

        start += batch
        time.sleep(1)  # polite delay

    return jobs


def print_jobs(jobs: list[dict]) -> None:
    if not jobs:
        print("Nenhuma oferta encontrada.")
        return

    print(f"\n{'='*70}")
    print(f"  {len(jobs)} oferta(s) encontrada(s)")
    print(f"{'='*70}\n")

    for i, job in enumerate(jobs, 1):
        print(f"[{i}] {job['titulo']}")
        print(f"    Empresa   : {job['empresa']}")
        print(f"    Localização: {job['localização']}")
        print(f"    Publicado : {job['data']}")
        print(f"    Link      : {job['link']}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Pesquisa de empregos no LinkedIn (Suíça)")
    parser.add_argument("keywords", nargs="?", default="", help="Palavras-chave (ex: 'python developer')")
    parser.add_argument("--location", default="Switzerland", help="Localização (default: Switzerland)")
    parser.add_argument("--max", type=int, default=20, help="Número máximo de resultados (default: 20)")
    args = parser.parse_args()

    print(f"A pesquisar: '{args.keywords or 'todas as áreas'}' em {args.location}...")
    jobs = fetch_jobs(args.keywords, args.location, args.max)
    print_jobs(jobs)


if __name__ == "__main__":
    main()
