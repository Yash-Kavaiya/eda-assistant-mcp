FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project metadata and source
COPY pyproject.toml .
COPY server.py .

# Build and install the MCP server with its dependencies
RUN pip install --no-cache-dir build \
    && python -m build \
    && pip install --no-cache-dir dist/*.whl \
    && rm -rf /root/.cache

# Expose ports if FastMCP uses HTTP transport (optional)
# EXPOSE 8000

# Start the server using stdio transport
CMD ["python", "server.py"]
