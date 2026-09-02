export interface User {
  user_name: string;
  first_name: string;
  last_name: string;
  email: string;
}

export async function Me(): Promise<User> {
  const response = await fetch("/api/user/me/", {
    credentials: 'include',
  });

  if (!response.ok) {
    throw new Error('Failed to fetch current user');
  }

  return (await response.json()) as User;
}