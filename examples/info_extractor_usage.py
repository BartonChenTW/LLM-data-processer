"""
InfoExtractor Usage Examples

Demonstrates structured information extraction from text sources using custom Pydantic schemas.
"""

from llm_helper import InfoExtractor
from typing import Dict, Any


def example_1_basic_extraction():
    """Example 1: Basic company information extraction."""
    print("=" * 70)
    print("Example 1: Basic Company Information Extraction")
    print("=" * 70)
    
    # Initialize extractor
    extractor = InfoExtractor(api_provider='google', model='gemini-2.5-flash')
    
    # Define schema
    schema = {
        'tech_type': 'CompanyInfo',
        'fields': {
            'name': {'field_type': 'str', 'description': 'Company name'},
            'founded_year': {'field_type': 'int', 'description': 'Year founded'},
            'industry': {'field_type': 'str', 'description': 'Primary industry'},
            'products': {'field_type': 'List[str]', 'description': 'Main products/services'},
            'headquarters': {'field_type': 'str', 'description': 'Headquarters location'}
        }
    }
    
    # Configure prompts
    base_prompts = {
        'system': 'You are an expert at extracting structured company information.',
        'human': '''Extract company information for {technology_name} from the following source:

{info_source}

Return the data in this format:
{format_instructions}'''
    }
    
    fix_prompts = {
        'system': 'You are an expert at fixing malformed JSON outputs.',
        'human': '''The following output for {technology_name} has formatting errors:

{malformed_output}

Fix it to match this format:
{format_instructions}'''
    }
    
    # Setup extractor
    extractor.load_data_schema(schema)
    extractor.load_prompt_templates(base_prompts, fix_prompts)
    
    # Source information
    company_info = """
    Tesla, Inc. was founded in 2003 by Martin Eberhard and Marc Tarpenning, 
    though Elon Musk is often associated with the company's early success.
    The company is headquartered in Austin, Texas. Tesla produces electric vehicles 
    including the Model S, Model 3, Model X, and Model Y. They also manufacture 
    battery energy storage systems and solar panels through Tesla Energy.
    """
    
    # Extract information
    extractor.load_info_source('Tesla', company_info)
    
    try:
        result = extractor.extract_tech_info(max_retries=3)
        
        print(f"\n✓ Successfully extracted information:\n")
        print(f"Company: {result.name}")
        print(f"Founded: {result.founded_year}")
        print(f"Industry: {result.industry}")
        print(f"Products: {', '.join(result.products)}")
        print(f"Headquarters: {result.headquarters}")
        
    except Exception as e:
        print(f"\n✗ Extraction failed: {e}")
    
    print()


def example_2_database_comparison():
    """Example 2: Extract and compare multiple database technologies."""
    print("=" * 70)
    print("Example 2: Database Technology Comparison")
    print("=" * 70)
    
    # Initialize extractor
    extractor = InfoExtractor(api_provider='google')
    
    # Define database schema
    schema = {
        'tech_type': 'DatabaseTechnology',
        'fields': {
            'name': {'field_type': 'str', 'description': 'Database name'},
            'type': {'field_type': 'str', 'description': 'Database type (SQL/NoSQL/etc)'},
            'description': {'field_type': 'str', 'description': 'Brief description'},
            'advantages': {'field_type': 'List[str]', 'description': 'Key advantages'},
            'use_cases': {'field_type': 'List[str]', 'description': 'Common use cases'},
            'scalability': {'field_type': 'str', 'description': 'Scalability characteristics'}
        }
    }
    
    # Configure prompts
    base_prompts = {
        'system': 'You are an expert at extracting structured database technology information.',
        'human': '''Extract information about {technology_name} from:

{info_source}

Format: {format_instructions}'''
    }
    
    fix_prompts = {
        'system': 'Fix malformed JSON to match the database schema.',
        'human': '''Fix this output for {technology_name}:

{malformed_output}

Expected format: {format_instructions}'''
    }
    
    # Setup
    extractor.load_data_schema(schema)
    extractor.load_prompt_templates(base_prompts, fix_prompts)
    
    # Database information sources
    databases = {
        'PostgreSQL': """
            PostgreSQL is a powerful, open-source object-relational database system.
            It's known for reliability, data integrity, and correctness. PostgreSQL 
            excels at handling complex queries and supports advanced data types. 
            Common use cases include web applications, data warehousing, and geospatial 
            applications. It scales well vertically and can be configured for horizontal 
            scaling with extensions.
        """,
        'MongoDB': """
            MongoDB is a document-oriented NoSQL database. It stores data in flexible, 
            JSON-like documents. MongoDB is designed for ease of development and scaling. 
            Its advantages include flexible schema, horizontal scalability, and rich query 
            language. Common use cases are content management, mobile apps, real-time analytics, 
            and IoT applications. MongoDB excels at horizontal scaling through sharding.
        """,
        'Redis': """
            Redis is an in-memory data structure store, used as a database, cache, and 
            message broker. It supports various data structures like strings, hashes, and lists. 
            Redis offers exceptional performance with sub-millisecond latency. Key advantages 
            include speed, atomic operations, and built-in replication. Use cases include 
            caching, session management, real-time analytics, and message queues. Redis scales 
            through clustering and replication.
        """
    }
    
    # Extract from each database
    results = []
    for db_name, db_info in databases.items():
        print(f"\nExtracting information for {db_name}...")
        extractor.load_info_source(db_name, db_info)
        
        try:
            result = extractor.extract_tech_info(max_retries=3)
            results.append(result)
            print(f"✓ Successfully extracted {db_name}")
        except Exception as e:
            print(f"✗ Failed to extract {db_name}: {e}")
    
    # Display comparison
    print("\n" + "=" * 70)
    print("COMPARISON RESULTS")
    print("=" * 70)
    
    for db in results:
        print(f"\n{db.name} ({db.type})")
        print(f"  Description: {db.description[:80]}...")
        print(f"  Advantages: {', '.join(db.advantages[:2])}...")
        print(f"  Use Cases: {', '.join(db.use_cases[:2])}...")
        print(f"  Scalability: {db.scalability}")
    
    print()


def example_3_with_validation():
    """Example 3: Extraction with setup validation and error handling."""
    print("=" * 70)
    print("Example 3: Extraction with Validation and Error Handling")
    print("=" * 70)
    
    # Initialize
    extractor = InfoExtractor(api_provider='google')
    
    # Define schema
    schema = {
        'tech_type': 'ProgrammingLanguage',
        'fields': {
            'name': {'field_type': 'str', 'description': 'Language name'},
            'paradigm': {'field_type': 'str', 'description': 'Programming paradigm'},
            'year_created': {'field_type': 'int', 'description': 'Year created'},
            'features': {'field_type': 'List[str]', 'description': 'Key features'},
            'popular_frameworks': {'field_type': 'List[str]', 'description': 'Popular frameworks'}
        }
    }
    
    # Configure
    extractor.load_data_schema(schema)
    
    base_prompts = {
        'system': 'Extract programming language information.',
        'human': 'Extract {technology_name} from: {info_source}\n{format_instructions}'
    }
    
    fix_prompts = {
        'system': 'Fix malformed JSON.',
        'human': 'Fix: {malformed_output}\nFormat: {format_instructions}'
    }
    
    extractor.load_prompt_templates(base_prompts, fix_prompts)
    
    # Validate setup before extraction
    print("\nValidating setup...")
    try:
        extractor.validate_setup()
        print("✗ Validation should have failed (no info source loaded)")
    except ValueError as e:
        print(f"✓ Validation correctly caught missing setup:\n  {str(e)[:100]}...")
    
    # Load information source
    python_info = """
    Python is a high-level, interpreted programming language created by Guido van Rossum 
    in 1991. It emphasizes code readability and supports multiple programming paradigms 
    including procedural, object-oriented, and functional programming. Key features include 
    dynamic typing, automatic memory management, and extensive standard library. Popular 
    frameworks include Django and Flask for web development, NumPy and pandas for data 
    analysis, and TensorFlow and PyTorch for machine learning.
    """
    
    extractor.load_info_source('Python', python_info)
    
    # Validate again
    print("\nValidating setup after loading source...")
    try:
        extractor.validate_setup()
        print("✓ Setup validation passed")
    except ValueError as e:
        print(f"✗ Validation failed: {e}")
        return
    
    # Extract with error handling
    print("\nExtracting information...")
    try:
        result = extractor.extract_tech_info(max_retries=3)
        
        print("\n✓ Extraction successful:\n")
        print(f"Language: {result.name}")
        print(f"Paradigm: {result.paradigm}")
        print(f"Created: {result.year_created}")
        print(f"Features: {', '.join(result.features[:3])}...")
        print(f"Frameworks: {', '.join(result.popular_frameworks[:3])}...")
        
    except Exception as e:
        print(f"\n✗ Extraction failed: {e}")
    
    print()


def example_4_batch_processing():
    """Example 4: Batch process multiple items efficiently."""
    print("=" * 70)
    print("Example 4: Batch Processing Multiple Technologies")
    print("=" * 70)
    
    def batch_extract(tech_data: Dict[str, str], schema: dict) -> list:
        """Helper function for batch extraction."""
        extractor = InfoExtractor(api_provider='google')
        extractor.load_data_schema(schema)
        
        base_prompts = {
            'system': 'Extract structured technology information.',
            'human': 'Extract {technology_name} from: {info_source}\n{format_instructions}'
        }
        
        fix_prompts = {
            'system': 'Fix malformed JSON output.',
            'human': 'Fix: {malformed_output}\nFormat: {format_instructions}'
        }
        
        extractor.load_prompt_templates(base_prompts, fix_prompts)
        
        results = []
        for name, info in tech_data.items():
            print(f"\nProcessing {name}...")
            try:
                extractor.load_info_source(name, info)
                result = extractor.extract_tech_info(max_retries=3)
                results.append(result)
                print(f"✓ {name} processed successfully")
            except Exception as e:
                print(f"✗ {name} failed: {str(e)[:50]}...")
        
        return results
    
    # Define schema for cloud services
    schema = {
        'tech_type': 'CloudService',
        'fields': {
            'name': {'field_type': 'str', 'description': 'Service name'},
            'provider': {'field_type': 'str', 'description': 'Cloud provider'},
            'category': {'field_type': 'str', 'description': 'Service category'},
            'features': {'field_type': 'List[str]', 'description': 'Key features'}
        }
    }
    
    # Technology data
    cloud_services = {
        'AWS Lambda': "AWS Lambda is a serverless compute service from Amazon. It runs code in response to events and automatically manages compute resources.",
        'Google Cloud Run': "Cloud Run is a managed compute platform by Google that runs containers. It automatically scales and charges only for resources used.",
        'Azure Functions': "Azure Functions is Microsoft's serverless compute service. It enables event-driven code execution without infrastructure management."
    }
    
    # Batch process
    results = batch_extract(cloud_services, schema)
    
    # Display results
    print("\n" + "=" * 70)
    print("BATCH PROCESSING RESULTS")
    print("=" * 70)
    
    for service in results:
        print(f"\n{service.name}")
        print(f"  Provider: {service.provider}")
        print(f"  Category: {service.category}")
        print(f"  Features: {', '.join(service.features[:3])}...")
    
    print()


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("InfoExtractor Usage Examples")
    print("=" * 70)
    print("\nThese examples demonstrate structured information extraction")
    print("from text sources using custom Pydantic schemas.\n")
    
    # Run examples
    example_1_basic_extraction()
    input("Press Enter to continue to Example 2...")
    
    example_2_database_comparison()
    input("Press Enter to continue to Example 3...")
    
    example_3_with_validation()
    input("Press Enter to continue to Example 4...")
    
    example_4_batch_processing()
    
    print("=" * 70)
    print("All examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()
