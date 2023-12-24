import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="flex fixed bottom-0 flex-col justify-center items-center p-4 w-full">
      <h3 className="text-sm font-nunito font-semibold opacity-25 text-center">
        projeto desenvolvido por{' '}
        <Link
          href="https://github.com/bernardomrl"
          className="link link-hover "
        >
          @bernardomrl
        </Link>{' '}
        e{' '}
        <Link href="https://github.com/nunes262" className="link link-hover ">
          @nunes262
        </Link>
      </h3>
    </footer>
  );
}
