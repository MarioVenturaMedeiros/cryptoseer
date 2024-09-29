# Docker

A aplicação é composta por quatro serviços principais: frontend, backend, PocketBase, e PostgreSQL. Cada um desses serviços é executado em um container separado, que contém todas as dependências necessárias para o seu funcionamento. Essa separação facilita a manutenção, o desenvolvimento paralelo e a atualização de componentes sem impactar os demais.

    Frontend: O frontend é um serviço React que está definido no container cryptoseer-frontend. Ele comunica-se com o backend através do endereço NEXT_PUBLIC_BACKEND_URL, que aponta para o serviço backend. O frontend é responsável por renderizar a interface de usuário e interagir com os serviços de backend através de chamadas HTTP.

    Backend: O backend é uma API desenvolvida em Python (utilizando FastAPI) que é responsável pelo processamento dos dados e por servir a lógica de negócio. O container cryptoseer-backend interage com o banco de dados PostgreSQL para operações de armazenamento e recuperação, além de acessar o PocketBase para gerenciar outras informações necessárias à aplicação. As variáveis de ambiente são utilizadas para definir a URL de acesso ao banco de dados e ao PocketBase.

    PocketBase: O PocketBase é utilizado para gerenciar dados específicos que não estão armazenados no banco de dados principal PostgreSQL. Ele possui um volume dedicado (./pocketbase_data:/app/pb_data) para garantir a persistência dos dados, mesmo que o container seja reiniciado.

    PostgreSQL: O banco de dados relacional PostgreSQL é usado para armazenar informações estruturadas, como dados de usuários e registros da aplicação. O container cryptoseer-postgres utiliza volumes para persistir dados entre reinicializações, o que garante que nenhuma informação seja perdida.

Rede e Comunicação Entre Containers

Todos os containers estão conectados à rede app-tier, que usa o driver bridge. Isso cria uma rede interna isolada onde os containers podem se comunicar de maneira segura e eficiente. Essa abordagem garante que o backend possa acessar o banco de dados PostgreSQL e o PocketBase diretamente, utilizando seus nomes de serviço (postgres e pocketbase), sem necessidade de expor as portas para fora do ambiente de Docker, aumentando a segurança.
Reinicialização e Persistência

Cada serviço possui uma política de reinicialização configurada como unless-stopped, o que significa que os containers serão reiniciados automaticamente caso ocorram falhas, garantindo alta disponibilidade da aplicação. Além disso, tanto o banco de dados PostgreSQL quanto o PocketBase utilizam volumes de armazenamento para garantir que os dados sejam persistidos mesmo que os containers sejam destruídos ou reiniciados.
Benefícios da Arquitetura

    Isolamento: Cada componente do sistema é executado em seu próprio container, o que evita conflitos de dependências e facilita o desenvolvimento e a depuração.
    Escalabilidade: Como os serviços são isolados, é fácil escalar cada componente de acordo com a demanda. Por exemplo, o frontend e o backend podem ser escalados horizontalmente sem impacto no banco de dados.
    Portabilidade: Toda a configuração do ambiente está definida no docker-compose.yml. Isso significa que a aplicação pode ser executada em qualquer ambiente que suporte Docker, independentemente das configurações específicas do sistema operacional subjacente.

Essa arquitetura baseada em Docker Compose é bastante eficiente para desenvolvimento e implantação de aplicações distribuídas, pois facilita a orquestração dos componentes e garante consistência em diferentes ambientes (desenvolvimento, teste e produção).