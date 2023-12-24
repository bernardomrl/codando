interface Props {
  children: React.ReactNode;
  title?: string;
}

export default function Section({ children, title }: Props) {
  return (
    <section className="flex h-screen w-screen flex-col items-center justify-center space-y-12">
      {title && (
        <h1 className="font-poppins text-xl font-bold leading-none">{title}</h1>
      )}
      {children}
    </section>
  );
}
