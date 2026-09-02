"use client";

import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { login } from "./_lib/login";

export default function Home() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [redirectTo] = useState(() => searchParams.get("redirectTo") ?? "/");
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.SubmitEvent) {
    e.preventDefault();
    setError(null);

    const result = await login(userName, password);
    if (!result.success) {
      setError(result.message ?? "Login failed");
      return;
    }

    router.push(redirectTo);
  }

  return (
    <div>
      <h1>This is Login page</h1>
      <form onSubmit={handleSubmit}>
        <p>User Name</p>
        <input
          id="user_name"
          type="text"
          value={userName}
          onChange={(e) => setUserName(e.target.value)}
          required
        />
        <p>Password</p>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
