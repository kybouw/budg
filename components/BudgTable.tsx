"use client";
import {
  Card,
  Table,
  TableHead,
  TableHeaderCell,
  TableBody,
  TableRow,
  TableCell,
  NumberInput,
  TableFoot,
  TableFooterCell,
} from "@tremor/react";
import { useEffect, useState } from "react";

export interface LineItem {
  name: string;
  value: number;
}

export default function BudgTable() {
  const totalPoints = 100;

  const [budgetAmount, setBudgetAmount] = useState(0);

  const [pointsUsed, setPointsUsed] = useState(0);
  const [pointsRemaining, setPointsRemaining] = useState(totalPoints - pointsUsed);
  const [data, setData] = useState([
    { name: "needs", value: 0 },
    { name: "invest", value: 0 },
    { name: "fun", value: 0 },
    { name: "give", value: 0 },
  ]);

  // whenever the number of used points updates, we need to calculate the points remaining
  useEffect(() => {
    setPointsRemaining(totalPoints - pointsUsed);
  }, [pointsUsed, totalPoints]);

  // whenever data is changed, we need to recalculate how many points we are using.
  useEffect(() => {
    setPointsUsed(data.reduce((sum, current) => sum + current.value, 0));
  }, [data]);

  const editData = (name: string, newValue: number) => {
    const newData = data.map((item: LineItem) => {
      if (item.name === name) {
        const newItem = {
          ...item,
          value: newValue,
        };
        return newItem;
      } else {
        return item;
      }
    });
    setData(newData);
  };

  const LineItemNode = (item: LineItem) => {
    const name = item.name;
    const [itemValue, setItemValue] = useState(item.value);
    useEffect(() => {
      editData(name, itemValue);
    }, [itemValue, name]);

    return (
      <TableRow key={name}>
        <TableCell>{name}</TableCell>
        <TableCell>
          <NumberInput value={itemValue} onValueChange={setItemValue} min={0} />
        </TableCell>
        <TableCell>{budgetAmount * (itemValue / 100)}</TableCell>
      </TableRow>
    );
  };

  return (
    <Card>
      <Table>
        <TableHead>
          <TableRow>
            <TableHeaderCell>Name</TableHeaderCell>
            <TableHeaderCell>Percentage</TableHeaderCell>
            <TableHeaderCell>Amount</TableHeaderCell>
          </TableRow>
        </TableHead>
        <TableBody>{data.map(LineItemNode)}</TableBody>
        <TableFoot>
          <TableRow>
            <TableFooterCell>Total</TableFooterCell>
            <TableCell>
              {pointsUsed}% Used / {pointsRemaining}% Remaining
            </TableCell>
            <TableCell>
              <NumberInput value={budgetAmount} onValueChange={setBudgetAmount} min={0} />
            </TableCell>
          </TableRow>
        </TableFoot>
      </Table>
    </Card>
  );
}
