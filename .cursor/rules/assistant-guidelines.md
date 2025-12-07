# Cursor Rules for Django Smart Export

## Language and Framework
- Always respond in French
- Use Django best practices and conventions
- Follow PEP 8 for Python code style
- Use type hints when appropriate

## Project Context
Django Smart Export est une application Django pour générer dynamiquement des exports PDF, CSV, Excel, JSON et TXT à partir de configurations stockées en base de données. Le projet se concentre sur :
- Les backends d'export : CSV, Excel, PDF, JSON, TXT
- La configuration dynamique des exports via des modèles Django
- Les vues et URLs pour déclencher les exports
- L'administration Django pour gérer les configurations

## Code Style
- Use black for code formatting (line length: 88)
- Use ruff for linting
- Prefer f-strings over .format() or % formatting
- Use pathlib.Path instead of os.path when possible
- Prefer list/dict comprehensions when readable

## Django ORM Specific
- Use Django ORM instead of raw SQL when possible
- Use select_related() and prefetch_related() to optimize queries
- Use F() expressions for database-level operations
- Use Q objects for complex queries
- Always use migrations for schema changes
- Use get_object_or_404() instead of try/except for single objects

## Export Backends
- Each backend (CSV, Excel, PDF, JSON, TXT) should have a consistent interface
- Handle large datasets efficiently (streaming, chunking)
- Provide proper error handling for each backend
- Support custom formatting and styling when applicable
- Document backend-specific requirements and limitations

## File Handling
- Use context managers for file operations
- Clean up temporary files after export
- Handle file encoding properly (UTF-8 for text files)
- Stream large files instead of loading everything in memory
- Use appropriate file extensions and MIME types

## Configuration Management
- Validate export configurations before use
- Provide sensible defaults for missing configuration
- Support dynamic field selection and ordering
- Handle field mappings and transformations
- Document configuration options clearly

## Performance
- Optimize database queries (avoid N+1 queries)
- Use annotations and aggregations when possible
- Consider using select_related/prefetch_related
- Stream large exports instead of loading all data in memory
- Use generators for large datasets
- Consider background tasks (Celery) for very large exports

## Security
- Never trust user input - always validate and sanitize
- Use Django's built-in security features (CSRF, XSS protection)
- Use parameterized queries (Django ORM handles this)
- Never commit secrets or API keys to version control
- Use environment variables for sensitive configuration
- Validate file paths to prevent directory traversal
- Limit file sizes to prevent DoS attacks
- Sanitize filenames to prevent security issues

## Testing
- Write tests for new export backends
- Use pytest and pytest-django for testing
- Test edge cases and error conditions
- Test with various data types and formats
- Test file generation and cleanup
- Use factories (factory_boy) for test data when appropriate
- Test with large datasets to ensure performance

## Documentation
- Write docstrings for functions and classes
- Use clear, descriptive variable and function names
- Add comments for complex export logic
- Document backend requirements (libraries, dependencies)
- Keep README.md up to date with examples
- Document configuration options and examples

## Git
- Write clear, descriptive commit messages
- Use conventional commits format when possible
- Keep commits focused and atomic

## Error Handling
- Use specific exception types
- Provide meaningful error messages
- Log errors appropriately
- Don't swallow exceptions silently
- Handle file I/O errors gracefully
- Provide user-friendly error messages for export failures

## Code Organization
- Keep functions small and focused
- Use Django apps to organize related functionality
- Separate export logic from view logic
- Use managers and querysets for complex queries
- Group backend implementations in the backends module

## Dependencies
- Keep dependencies up to date
- Use requirements.txt or pyproject.toml for dependencies
- Pin versions for production
- Document why each dependency is needed
- Note backend-specific dependencies (openpyxl, reportlab, etc.)

## Export Backend Specific
- CSV: Handle special characters, encoding, delimiters
- Excel: Support formatting, multiple sheets, large files
- PDF: Handle page breaks, styling, fonts, images
- JSON: Validate JSON structure, handle nested data
- TXT: Handle encoding, line breaks, formatting

## View and URL Patterns
- Use class-based views when appropriate
- Handle authentication and permissions
- Provide download links and preview options
- Support filtering and pagination for large datasets
- Handle async exports for long-running operations

## Admin Interface
- Provide intuitive admin interface for configuration
- Support preview of export configurations
- Validate configurations in admin forms
- Provide helpful error messages
- Support bulk operations when applicable

## Memory Management
- Use generators for large datasets
- Stream file generation when possible
- Clean up temporary files promptly
- Monitor memory usage for large exports
- Consider chunking for very large datasets

