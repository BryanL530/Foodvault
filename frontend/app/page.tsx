import Image from "next/image";
var isLoggedIn = true;

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <h1>Home Page</h1>
      <p>User is {isLoggedIn ? 'Logged in' : 'Logged out'}</p>
      <button type="button"></button>
    </div>
  );
}
