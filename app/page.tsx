import BudgTable from "@/components/BudgTable";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col p-24">
      <h1 className="text-4xl font-bold mb-12">Budg</h1>
      <BudgTable />
      <div></div>
    </main>
  );
}
