"use client";
import { use, useEffect, useState } from "react";

export default function VaultPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // fetch the vault's data using `id` here
    setLoading(false);
  }, [id]);

  return (
    <div>
      <section>
        <h1>Vault {id}</h1>
        <p>XXX Members • XXX Items</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque odit, dolor sapiente inventore magnam fugit, maiores laudantium, libero unde consequuntur quidem tenetur ducimus quos minima voluptatem quas officiis doloribus explicabo.</p>
        <button>Settings</button>
      </section>
      <section>
        <p>Filters buttons</p>
        <input type="search" name="item-search" id="item-search" placeholder="search"/>
        <p>Expiration Date</p>
      </section>
      <table>
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Count</th>
            <th scope="col">Expiration Date</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">Apple</th>
            <td>20</td>
            <td>09-11-26</td>
          </tr>
          <tr>
            <th scope="row">Beagal</th>
            <td>30</td>
            <td>10-11-26</td>
          </tr>
          <tr>
            <th scope="row">Cabbage</th>
            <td>3</td>
            <td>09-17-26</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
