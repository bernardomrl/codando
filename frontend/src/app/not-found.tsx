import Link from 'next/link';

const links = [
  {
    name: 'Página Inicial',
    route: '/'
  },
  {
    name: 'Suporte',
    route: 'mailto:bernardomrl@icloud.com'
  }
];

export default function Index() {
  return (
    <main className="h-screen w-full flex flex-col justify-center items-center">
      <p className="text-base font-bold font-nunito text-accent">404</p>
      <h1 className="mt-4 text-3xl font-bold font-poppins tracking-tightsm:text-5xl">
        Página não encontrada
      </h1>
      <p className="mt-6 text-lg leading-7 font-nunito font-semibold">
        Desculpe, não conseguimos encontrar a página que você está procurando.
      </p>
      <div className="mt-10 flex items-center justify-center gap-x-6">
        {links.map((item, index) => (
          <Link
            href={item.route}
            key={index}
            className="btn btn-sm btn-outline btn-accent w-full max-w-md font-nunito normal-case font-semibold"
          >
            {item.name}
          </Link>
        ))}
      </div>
    </main>
  );
}
