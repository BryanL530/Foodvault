"use client";

import { useEffect, useState } from "react";
import { Me, type User } from "@/app/lib/user";

export default function Home() {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Me()
      .then(setUser)
      .catch(() => setUser(null))
      .finally(() => setLoading(false));
  }, []);

  const isLoggedIn = user !== null;

  return (
    <div>
      <h1>Home Page</h1>
      <p>
        {loading ? "Loading..." : isLoggedIn
          ? `Logged in as ${user.user_name}`: "Logged out"}
      </p>
      {isLoggedIn ? <button>Logout</button> : <button>Login</button>}
    </div>
  );
}
