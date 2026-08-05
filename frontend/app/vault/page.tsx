import { Metadata } from "next";

export const metadata: Metadata = {
  title:"Vault"
};

export default function vault() {
  return (
    <>
      <h1>Vault</h1>
      <div className="vault-container">
        <div className="vault-card">
          <h2>Vault name</h2> 
          <p>100 Items</p>
        </div>
      </div>
    </>
  );
};