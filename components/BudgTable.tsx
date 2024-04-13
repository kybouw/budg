import LineItem from "@/components/LineItem";

export default function BudgTable() {
  const lineItems = ["Needs", "Invest", "Fun", "Give"];
  const lineItemNodes = lineItems.map((item) => {
    return <LineItem key={item} name={item} />;
  });

  return <ul>{lineItemNodes}</ul>;
}
