movies = {
    # A dict defining the actual data structure being handled by the resource.
    # Enables data validation.
    'schema': {
        'title': {
            'type': 'string',
            'minlength': 1,
            'unique': True,
            'required': True
        },
        'description': {
            'type': 'string',
        }
    }
}
