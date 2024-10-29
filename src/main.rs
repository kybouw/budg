use std::fs;

use rust_decimal_macros::dec;
use toml::Table;

const MAX_WIDTH: i32 = 30;

fn print_divider() {
    for _ in 1..MAX_WIDTH {
        print!("=")
    }
    println!("")

}
fn main() {
    let plan_file_contents = fs::read_to_string("static/default.toml").expect("failed to read static/default.toml");
    let plan_table = plan_file_contents.parse::<Table>().expect("failed to parse table");

    let budget_total = dec!(500);
    
    for (major_label, minor_table) in plan_table {
        print_divider();
        let major_budget_total = dec!(0);

        // TODO unwrap Value enum into String (for 1-level plan) or Table (for 2-level plan)
        // for (minor_label, minor_value) in minor_table {
            
        // }
    }
}
