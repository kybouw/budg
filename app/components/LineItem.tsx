export interface LineItemProps {
  name: string;
}

export default function LineItem({ name }: LineItemProps) {
  return <li>{name}</li>;
}
