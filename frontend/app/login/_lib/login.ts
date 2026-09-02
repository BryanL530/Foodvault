export interface LoginResult {
  success: boolean;
  message?: string;
}

export async function login(
  user_name: string,
  password: string,
): Promise<LoginResult> {
  const response = await fetch("/api/login/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ user_name, password }),
  });

  
  const data = (await response.json()) as { message?: string };
  if (!response.ok) {
    return { success: false, message: data.message ?? "Login failed" };
  }
  
  return { success: true, message: data.message };
}
