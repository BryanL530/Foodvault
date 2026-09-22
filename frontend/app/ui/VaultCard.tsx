import Link from "next/link";

export interface Vault {
  id: number;
  name: string;
  description: string;
}

export function VaultCard({ vault }: { vault: Vault }) {
  return (
    <Link href={`/vault/${vault.id}`}>
      <h3>{vault.name}</h3>
      <p>{vault.description}</p>
    </Link>
  );
}
