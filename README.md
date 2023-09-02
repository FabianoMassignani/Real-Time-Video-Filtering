# Aplicativo de Filtragem de Vídeo com Trackbars

Este é um aplicativo Python que usa a biblioteca OpenCV para capturar vídeo da câmera e aplicar filtros de processamento de imagem em tempo real. O aplicativo permite que o usuário ajuste os parâmetros dos filtros usando trackbars.

## Funcionalidades

- **Captura de Vídeo**: O aplicativo captura vídeo da câmera em tempo real.

- **Filtros Passa-Baixa**: O usuário pode ajustar os parâmetros dos filtros passa-baixa (Blur e Gaussian) usando trackbars.

- **Filtro Passa-Alta**: O aplicativo aplica um filtro passa-alta Laplaciano para realçar as bordas da imagem.

- **Binarização**: O resultado do filtro Laplaciano é binarizado para destacar as bordas da imagem.

- **Exibição ao Vivo**: O vídeo processado é exibido em uma janela em tempo real.

- **Encerramento do Aplicativo**: O aplicativo pode ser encerrado pressionando a tecla 'q'.

## Uso

1. Execute o código Python fornecido.
2. Uma janela chamada "Video" será aberta, exibindo a captura de vídeo da câmera.
3. Use as trackbars "Blur" e "Gaussian" para ajustar os parâmetros dos filtros passa-baixa.
4. O vídeo processado com os filtros e realce de bordas será exibido em tempo real na janela "Video".
5. Pressione a tecla 'q' para encerrar o aplicativo.

## Requisitos

```bash
pip install opencv-python
```

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

---
