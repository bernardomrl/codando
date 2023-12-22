import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Projeto Codando',
  description: 'Projeto Codando'
};

const buttons = [
  {
    name: 'Criar novo produto',
    route: '/create'
  },
  {
    name: 'Apagar produto',
    route: '/delete'
  },
  {
    name: 'Listar produtos',
    route: '/list'
  },
  {
    name: 'Atualizar produtos',
    route: '/update'
  }
];

export default function Index() {
  return (
    <main className="h-screen w-full flex flex-col justify-center items-center space-y-8  p-8">
      <div className="flex flex-col justify-center items-center space-y-4 w-full max-w-xs">
        {buttons.map((item, index) => (
          <Link
            href={item.route}
            key={index}
            className="btn btn-sm btn-outline btn-accent rounded-md font-nunito font-bold text-md normal-case w-full max-w-xs"
          >
            {item.name}
          </Link>
        ))}
      </div>
    </main>
  );
}
