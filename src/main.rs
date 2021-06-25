extern crate reqwest;
extern crate scraper;

use scraper::{Html, Selector};

fn main() {
    println!("the scraped data is : ");
    scrape_team_data("https://en.wikipedia.org/wiki/Main_Page");
}
fn scrape_team_data(url:&str) {
    let mut req = reqwest::get(url).unwrap();
    assert!(req.status().is_success());
    let doc_body = Html::parse_document(&req.text().unwrap());
    let team = Selector::parse(".mw-body").unwrap();

    for team in doc_body.select(&team) {
        let team = team.text().collect::<Vec<_>>();
        println!("{}", team[0]);
    }
}
