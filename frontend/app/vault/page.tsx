import { Vault, VaultCard } from "../ui/VaultCard"

const testVault: Vault = {id: 1234, name:'test name', description: 'test desc'};

export default function Home() {
  return (
    <>
      <h1>This is page for vault</h1>
      <h2>What needs to be done for this page:</h2>
      <ul>
        <li>List of vaults</li>
        <li>Clickable vaults</li>
      </ul>

      <VaultCard vault={testVault} />
    </>
  )
}