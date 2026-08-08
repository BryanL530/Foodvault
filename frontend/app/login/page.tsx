export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <h1>This is Login page</h1>
      <p>User Name</p>
      <input type='text' placeholder="test" required/>
      <p>Password</p>
      <input type='text' placeholder="test" required/>
      <button type="submit">Login</button>
    </div>
  );
}