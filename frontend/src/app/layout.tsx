import '@/styles/globals.css';

import { Footer } from '@/components';

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-br">
      <body>
        {children}
        <Footer />
      </body>
    </html>
  );
}
