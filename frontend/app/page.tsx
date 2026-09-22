"use client";

import { useEffect, useState } from "react";
import { useRouter, usePathname, useSearchParams } from "next/navigation";
import { FetchSelfData, type User } from "@/app/lib/user";

export default function Home() {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const goToLogin = () => {
    const query = searchParams.toString();
    const currentUrl = query ? `${pathname}?${query}` : pathname;
    router.push(`/login?redirectTo=${encodeURIComponent(currentUrl)}`);
  };
  const logout = async () => {
    const response = await fetch('/api/logout/', {
      method: 'POST',
      credentials: 'include',
    })

    if (!response.ok) {
      console.log('Something went wrong')
      return
    }

    setUser(null)
  }

  useEffect(() => {
    FetchSelfData()
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
      {isLoggedIn ? (
        <button onClick={logout}>Logout</button>
      ) : (
        <button onClick={goToLogin}>Login</button>
      )}
    </div>
  );
}
