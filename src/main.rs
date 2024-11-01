use std::fs;

use rust_decimal::Decimal;
use rust_decimal_macros::dec;
use toml::{Table, Value};

enum Divider {
    Dash,
    Equals,
}

fn print_divider(divider: Divider) {
    match divider {
        Divider::Dash => {
            println!("{:-^30}", "")
        }
        Divider::Equals => {
            println!("{:=^30}", "")
        }
    }
}

fn print_budget_line(total: Decimal, ratio: Decimal, name: String) -> Decimal {
    let value = (total * ratio).trunc_with_scale(2);
    println!("{:<20}${:>9}", name, value.to_string());
    return value;
}

fn calculate_budget(total: Decimal) {
    let plan_file_contents =
        fs::read_to_string("static/default.toml").expect("failed to read static/default.toml");
    let plan_table = plan_file_contents
        .parse::<Table>()
        .expect("failed to parse table");

    for (major_label, major_value) in plan_table {
        print_divider(Divider::Equals);

        match major_value {
            Value::Float(v) => {
                let d = Decimal::from_str_exact(&v.to_string()).expect("failed to parse decimal");
                print_budget_line(total, d / dec!(100), major_label);
            }
            Value::Integer(v) => {
                let d = Decimal::from_str_exact(&v.to_string()).expect("failed to parse decimal");
                print_budget_line(total, d / dec!(100), major_label);
            }
            Value::Table(t) => {
                let mut major_budget_total = dec!(0);
                for (minor_label, minor_value) in t {
                    let r = match minor_value {
                        Value::Float(v) => Decimal::from_str_exact(&v.to_string())
                            .expect("failed to parse decimal"),
                        Value::Integer(v) => Decimal::from_str_exact(&v.to_string())
                            .expect("failed to parse decimal"),
                        _ => panic!("not a number"),
                    } / dec!(100);
                    major_budget_total += print_budget_line(total, r, minor_label);
                }
                print_divider(Divider::Dash);
                println!(
                    "{:<20}${:>9}",
                    major_label,
                    major_budget_total.trunc_with_scale(2)
                )
            }
            _ => panic!("not a number"),
        }
    }
    print_divider(Divider::Equals);
}

fn main() {
    calculate_budget(dec!(500));
}
