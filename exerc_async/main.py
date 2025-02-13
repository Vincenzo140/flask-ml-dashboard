import asyncio
import time

# Função mostando uma chamada de rede
async def network_call(delay):
    await asyncio.sleep(delay)

async def main():
    start_time = time.time()  # Marca o tempo no inicio

    # Fazendo as chamadas de rede de forma assíncrona
    await asyncio.gather(
        network_call(2),  # Primeira chamada demora 2 segs
        network_call(3),  # Segunda chamada demora 3 segs
        network_call(1)   # Terceira chamada demora 1 segs
    )

    end_time = time.time()  # Marca o tempo de fim
    return end_time - start_time  # Retorna o tempo total de execução

# Executa a função
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    total_time = loop.run_until_complete(main())
    print(f"Tempo total: {total_time:.2f} segundos")
