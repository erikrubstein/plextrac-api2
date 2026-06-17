"""Generated from the public PlexTrac Postman collection.

Do not edit by hand. Run scripts/generate_endpoints.py to refresh.
"""

GROUPS = {'admin': {'display_name': 'Admin',
           'endpoints': [{'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Return a list of supported authentication '
                                         'providers</p>\n',
                          'folder_path': ['Admin', 'Auth'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_available_authentication_providers',
                          'name': 'Get Available Authentication Providers',
                          'path': '/api/v2/authenticate/providers'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Admin only route, update authentication provider '
                                         'configuration</p>\n',
                          'folder_path': ['Admin', 'Auth'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_tenant_provider_authentication_configuration',
                          'name': 'Get Tenant Provider Authentication Configuration',
                          'path': '/api/v2/tenants/{tenantId}/providers/plextrac'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Update configuration for tenant authentication '
                                         'providers (Okta, Azure AD, Google) (Admin only)</p>\n',
                          'folder_path': ['Admin', 'Auth'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'update_tenant_authentication_provider_configuration',
                          'name': 'Update Tenant Authentication Provider Configuration',
                          'path': '/api/v2/tenants/{tenantId}/providers/plextrac'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Update the authentication method a tenant user is '
                                         'authorized to log in with (admin only)</p>\n',
                          'folder_path': ['Admin', 'Auth'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'update_tenant_user_authentication_method',
                          'name': 'Update Tenant User Authentication Method',
                          'path': '/api/v2/authenticate/tenants/{tenantId}/users/{userId}/configuration'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Endpoint for getting a single saml provider '
                                         'configuration, validate: {\n'
                                         '        params: {\n'
                                         '            tenantId: Joi.number()\n'
                                         '                .integer()\n'
                                         '                .required(),\n'
                                         '            providerName: Joi.string()\n'
                                         '                .required(),\n'
                                         '        },\n'
                                         '        failAction,\n'
                                         '    },\n'
                                         '    auth: {\n'
                                         "        scope: ['global_admin', "
                                         "'tenant_admin_{params.tenantId}'],\n"
                                         '    },</p>\n',
                          'folder_path': ['Admin', 'Auth'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_saml_provider',
                          'name': 'Get Saml Provider',
                          'path': '/api/v2/tenants/{tenantId}/saml/plextrac'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Endpoint for updating and creating saml providers for '
                                         'a tenant.</p>\n'
                                         '<p>params: {\n'
                                         '            tenantId: Joi.number()\n'
                                         '                .integer()\n'
                                         '                .required(),\n'
                                         '            providerName: Joi.string()\n'
                                         '                .required(),\n'
                                         '        },\n'
                                         '        payload: {\n'
                                         '            enabled: Joi.boolean().required(),\n'
                                         '            providerName: Joi.string().required(),\n'
                                         '            issuer: Joi.string().required(),\n'
                                         '            cert: Joi.string().required(),\n'
                                         '            idpSSOUrl: Joi.string().required(),\n'
                                         '        }</p>\n',
                          'folder_path': ['Admin', 'Auth'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'upsert_saml_configuration',
                          'name': 'Upsert Saml Configuration',
                          'path': '/api/v2/tenants/{tenantId}/saml/plextrac'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': "<p>Gets a user's RBAC permissions.</p>\n"
                                         '<p>This is only to get the RBAC permissions of the user '
                                         'that is authenticated to the API. Trying to user this '
                                         'for another user will return a 403 error with the '
                                         'message <code>"Not authorized to view user '
                                         'permissions"</code></p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC', 'Users'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_user_permissions',
                          'name': 'Get User Permissions',
                          'path': '/api/v2/tenants/{tenantId}/user/{userId}/permissions'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Gets all users associated with a certain RBAC '
                                         'security role.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC', 'Users'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_role_users',
                          'name': 'Get Role Users',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleKey}/users'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Adds a user to an RBAC Security Role.</p>\n'
                                         '<p><strong>Important:</strong> It is highly recommended '
                                         'to perform this action in the Plextrac platform. There '
                                         'is a permissions wizard that goes through multiple steps '
                                         'to make sure a user is assigned the correct permissions '
                                         'throughout the app.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC', 'Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'add_role_user',
                          'name': 'Add Role User',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleId}/users'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Removes a user from an RBAC security role.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC', 'Users'],
                          'graphql_query': None,
                          'method': 'DELETE',
                          'method_name': 'remove_role_user',
                          'name': 'Remove Role User',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleId}/users/{userId}'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Gets a list of RBAC security roles and returns the '
                                         '<code>name</code> and <code>CUID</code> of each '
                                         'role.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_available_security_roles',
                          'name': 'Get Available Security Roles',
                          'path': '/api/v2/tenants/{tenantId}/security/role/available'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Get a list of RBAC security roles.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_security_roles',
                          'name': 'Get Security Roles',
                          'path': '/api/v2/tenants/{tenantId}/security/role'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Gets an RBAC security role.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_security_role',
                          'name': 'Get Security Role',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleId}'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Determines availability for a new RBAC Security '
                                         'Role.</p>\n'
                                         '<p>The key value should have the format '
                                         '<code>TENANT_0_ROLE_[NAME_TO_CHECK]</code></p>\n'
                                         '<p>This is checking against a key generated from the '
                                         'name where letters are capital and spaces are replaced '
                                         'with underscores.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'get_role_name_availability',
                          'name': 'Get Role Name Availability',
                          'path': '/api/v2/tenants/{tenantId}/security/role/availability'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>Creates a new RBAC security role.</p>\n',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'create_security_role',
                          'name': 'Create Security Role',
                          'path': '/api/v2/tenants/{tenantId}/security/role'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': "<p>Updates a security role's info fields.</p>\n",
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'update_security_role_info',
                          'name': 'Update Security Role Info',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleId}/info'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'update_security_role_permission',
                          'name': 'Update Security Role Permission',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleId}/permissions'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '',
                          'folder_path': ['Admin', 'Security', 'RBAC'],
                          'graphql_query': None,
                          'method': 'DELETE',
                          'method_name': 'delete_security_role',
                          'name': 'Delete Security Role',
                          'path': '/api/v2/tenants/{tenantId}/security/role/{roleId}'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [('limit', '10'), ('offset', '0')],
                          'description': '<p>This request retrieves <strong>a list of all tags for '
                                         'a tenant</strong> with filter options.</p>\n',
                          'folder_path': ['Admin', 'Tags'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'list_tenant_tags',
                          'name': 'List Tenant Tags',
                          'path': '/api/v1/tenant/{tenantId}/tag'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request creates <strong>a new tag for a '
                                         'tenant.</strong> A created tag will be listed on the tag '
                                         'dropdown that appears when typing to add a tag anywhere '
                                         'in the platform. This functionality is found in the '
                                         'platform under Account Admin &gt; Tag Settings &gt; '
                                         'Create Tag</p>\n'
                                         '<p>The <code>scope</code> should be '
                                         '<code>"tenant"</code></p>\n'
                                         '<p>The <code>ownerId</code> is the '
                                         '<code>tenantId</code></p>\n'
                                         '<p>This endpoint returns an empty array <code>[]</code> '
                                         'when successful</p>\n',
                          'folder_path': ['Admin', 'Tags'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'create_tenant_tag',
                          'name': 'Create Tenant Tag',
                          'path': '/api/v1/tenant/{tenantId}/tag'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request creates <strong>a new tag for a '
                                         'tenant.</strong> This functionality is found in the '
                                         'platform under Account Admin &gt; Tag Settings &gt; '
                                         'Actions &gt; Delete</p>\n'
                                         '<p>The <code>tagId</code> should be a string with the '
                                         'format <code>tag_[scope]_[ownerId]_[name]</code> i.e. '
                                         '<code>tag_tenant_0_new_test_tag</code></p>\n',
                          'folder_path': ['Admin', 'Tags'],
                          'graphql_query': None,
                          'method': 'DELETE',
                          'method_name': 'delete_tenant_tag',
                          'name': 'Delete Tenant Tag',
                          'path': '/api/v1/tenant/{tenantId}/tag/{tagId}'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [('text', 'example'), ('limit', '20'), ('offset', '0')],
                          'description': '<p>This endpoint allows users to search for tags within '
                                         'a specific tenant.</p>\n'
                                         '<h4 id="request-parameters">Request Parameters</h4>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>text</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The text to search for within the tags</td>\n'
                                         '</tr>\n'
                                         '<tr>\n'
                                         '<td>limit</td>\n'
                                         '<td>Integer</td>\n'
                                         '<td>The maximum number of tags to retrieve '
                                         '(optional)</td>\n'
                                         '</tr>\n'
                                         '<tr>\n'
                                         '<td>offset</td>\n'
                                         '<td>Integer</td>\n'
                                         '<td>The number of tags to skip before starting to '
                                         'retrieve (optional)</td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><h4 id="response-fields">Response Fields</h4>\n'
                                         '<p>In the event of a successful request, the response '
                                         "will contain a 'count' array with the total number of "
                                         "matching tags and a 'tags' array with the list of tags. "
                                         'Each tag object will contain the following fields:</p>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>id</td>\n'
                                         '<td>String</td>\n'
                                         '<td>Unique identifier of the tag</td>\n'
                                         '</tr>\n'
                                         '<tr>\n'
                                         '<td>name</td>\n'
                                         '<td>String</td>\n'
                                         '<td>Name of the tag</td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><p>In the event of an error, the response will not '
                                         'contain any specific error fields.</p>\n',
                          'folder_path': ['Admin', 'Tags'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'search_tenant_tags',
                          'name': 'Search Tenant Tags',
                          'path': '/api/v1/tenant/{tenantId}/tag/search'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This endpoint allows developers to find a tag for a '
                                         'specific tenant.</p>\n'
                                         '<h4 id="request-parameters">Request Parameters</h4>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>tenantId</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The unique identifier of the tenant</td>\n'
                                         '</tr>\n'
                                         '<tr>\n'
                                         '<td></td>\n'
                                         '<td></td>\n'
                                         '<td></td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><h4 id="response-fields">Response Fields</h4>\n'
                                         '<p>In the event of a successful request, the response '
                                         'will contain an object with the following fields:</p>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>id</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The unique identifier of the tag</td>\n'
                                         '</tr>\n'
                                         '<tr>\n'
                                         '<td>name</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The name of the tag</td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><p>In the event of an error, the response will '
                                         "contain an 'error' object with a 'message' field "
                                         'describing the error.</p>\n',
                          'folder_path': ['Admin', 'Tags'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'find_tenant_tag',
                          'name': 'Find Tenant Tag',
                          'path': '/api/v1/tenant/{tenantId}/tag/find'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request retrieves <strong>all</strong> SLA '
                                         'benchamrks for a tenant.</p>\n'
                                         '<p>The <code>instanceUrl</code> is needed to execute the '
                                         'call.</p>\n',
                          'folder_path': ['Admin', 'SLAs'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_sla_benchmarks',
                          'name': 'Get SLA Benchmarks',
                          'path': '/api/v2/sla/benchmarks'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request <strong>creates</strong> a new SLA '
                                         'benchmark within a tenant.</p>\n'
                                         '<p>The <code>name</code>, <code>daysToClose</code>, '
                                         '<code>findingSeverity</code>, and <code>enabled</code> '
                                         'are required properties.</p>\n',
                          'folder_path': ['Admin', 'SLAs'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'create_sla_benchmark',
                          'name': 'Create SLA Benchmark',
                          'path': '/api/v2/sla/benchmarks'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request retrieves information on a SLA '
                                         'benchmark.</p>\n'
                                         '<h4 id="request-parameters">Request Parameters</h4>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>slaBenchmarkId</td>\n'
                                         '<td>Integer</td>\n'
                                         '<td>The ID of the SLA to retrieve</td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><p>A successsfull call returns the JSON object of '
                                         'the SLA benchmark stored in the DB.</p>\n',
                          'folder_path': ['Admin', 'SLAs'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_sla_benchmark',
                          'name': 'Get SLA Benchmark',
                          'path': '/api/v2/sla/benchmarks/{slaBenchmarkId}'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request updates an existing SLA benchamrk. This '
                                         'is a PUT request and will overwrite the current SLA with '
                                         'the new payload.</p>\n'
                                         '<h4 id="request-parameters">Request Parameters</h4>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>slaBenchmarkId</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The unique identifier of the SLA to be updated</td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><h4 id="request-payload">Request Payload</h4>\n'
                                         '<p>You should use the Get SLA Benchmark endpoint to get '
                                         'the SLA object, then use that JSON object as the '
                                         'payload.</p>\n'
                                         '<p>You must remove the <code>doc_type</code> and '
                                         '<code>tenant_id</code> properties before sending hte '
                                         'payload.</p>\n'
                                         '<h4 id="response-fields">Response Fields</h4>\n'
                                         '<p>In the event of a successful request, the response '
                                         'will contain the following fields:</p>\n'
                                         '<div class="click-to-expand-wrapper '
                                         'is-table-wrapper"><table>\n'
                                         '<thead>\n'
                                         '<tr>\n'
                                         '<th>Parameter</th>\n'
                                         '<th>Type</th>\n'
                                         '<th>Description</th>\n'
                                         '</tr>\n'
                                         '</thead>\n'
                                         '<tbody>\n'
                                         '<tr>\n'
                                         '<td>status</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The status of the request</td>\n'
                                         '</tr>\n'
                                         '<tr>\n'
                                         '<td>data</td>\n'
                                         '<td>String</td>\n'
                                         '<td>The ID of the SLA that was updated</td>\n'
                                         '</tr>\n'
                                         '</tbody>\n'
                                         '</table>\n'
                                         '</div><p>In the event of an error, the response will '
                                         "contain an 'error' object with a 'message' field "
                                         'describing the error.</p>\n',
                          'folder_path': ['Admin', 'SLAs'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'update_sla_benchmark',
                          'name': 'Update SLA Benchmark',
                          'path': '/api/v2/sla/benchmarks/{slaBenchmarkId}'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request <strong>removes</strong> a SLA benchmark '
                                         'from a tenant.</p>\n'
                                         '<p>The <code>instanceUrl</code> and '
                                         '<code>slaBenchamrkId</code> is needed to execute the '
                                         'call.</p>\n',
                          'folder_path': ['Admin', 'SLAs'],
                          'graphql_query': None,
                          'method': 'DELETE',
                          'method_name': 'delete_sla_benchmark',
                          'name': 'Delete SLA Benchmark',
                          'path': '/api/v2/sla/benchmarks/{slaBenchmarkId}'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [('limit', '5'), ('offset', '0')],
                          'description': '<p>This endpoint retrieves audit log data. The logs that '
                                         'show up under Admin Dashboard &gt; Security &amp; User '
                                         'Management &gt; Audit Logs are not the comprehensive app '
                                         'logs, but only a subset.  </p>\n'
                                         '<p><strong>Included Event Types:</strong></p>\n'
                                         '<ul>\n'
                                         '<li><p>LoginSuccess</p>\n'
                                         '</li>\n'
                                         '<li><p>LoginFail</p>\n'
                                         '</li>\n'
                                         '<li><p>LoginLockout</p>\n'
                                         '</li>\n'
                                         '<li><p>UserUnlocked</p>\n'
                                         '</li>\n'
                                         '<li><p>UserCreated</p>\n'
                                         '</li>\n'
                                         '<li><p>UserDeleted</p>\n'
                                         '</li>\n'
                                         '<li><p>UserEnabled</p>\n'
                                         '</li>\n'
                                         '<li><p>UserDisabled</p>\n'
                                         '</li>\n'
                                         '<li><p>PasswordChanged</p>\n'
                                         '</li>\n'
                                         '<li><p>PasswordChangedByOther</p>\n'
                                         '</li>\n'
                                         '<li><p>TenantRoleCreated</p>\n'
                                         '</li>\n'
                                         '<li><p>TenantRoleDeleted</p>\n'
                                         '</li>\n'
                                         '<li><p>TenantRoleUpdated</p>\n'
                                         '</li>\n'
                                         '<li><p>TenantRoleAssigned</p>\n'
                                         '</li>\n'
                                         '<li><p>TenantRoleRemoved</p>\n'
                                         '</li>\n'
                                         '<li><p>UserClientRoleAssigned</p>\n'
                                         '</li>\n'
                                         '<li><p>UserClientRoleRemoved</p>\n'
                                         '</li>\n'
                                         '<li><p>AddedToDefaultGroup</p>\n'
                                         '</li>\n'
                                         '<li><p>ClientLicenseUpdated</p>\n'
                                         '</li>\n'
                                         '<li><p>UserLicenseUpdated</p>\n'
                                         '</li>\n'
                                         '</ul>\n',
                          'folder_path': ['Admin', 'Audit Log'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_audit_log',
                          'name': 'Get Audit Log',
                          'path': '/api/v2/auditlog'}]},
 'affected_assets': {'display_name': 'Affected Assets',
                     'endpoints': [{'aliases': [],
                                    'body_mode': 'formdata',
                                    'default_params': [],
                                    'description': "<p>URL <strong>source</strong> accepts 'csv', "
                                                   "'xml'</p>\n"
                                                   '<p>File size limit 1gb file</p>\n',
                                    'folder_path': ['Affected Assets'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'import_finding_affected_assets',
                                    'name': 'Import Finding Affected Assets',
                                    'path': '/api/v2/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected-assets/import/{source}'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '',
                                    'folder_path': ['Affected Assets'],
                                    'graphql_query': None,
                                    'method': 'DELETE',
                                    'method_name': 'remove_affected_asset',
                                    'name': 'Remove Affected Asset from Flaw',
                                    'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>For affected assets on a report finding, '
                                                   'gets the most recent status tracker update for '
                                                   'each affected asset requested. Affected assets '
                                                   'without any status tracker update will not '
                                                   'return an entry in the reponse dict.</p>\n',
                                    'folder_path': ['Affected Assets'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_get_affected_asset_statuses',
                                    'name': 'Bulk Get Affected Assets Status',
                                    'path': '/api/v2/client/{clientId}/report/{reportId}/flaw/{findingId}/assets/status'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>Retrieves the list of all status tracker '
                                                   'updates for an affected asset.</p>\n',
                                    'folder_path': ['Affected Assets'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'list_affected_asset_status_updates',
                                    'name': 'Get Affected Asset Status List',
                                    'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>Adds a status tracker update for an '
                                                   'affected asset on a finding. The payload of '
                                                   'this request should be the entire finding '
                                                   'object retrieve from the <a '
                                                   'href="https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc">Get '
                                                   'Findings</a> endpoint.</p>\n'
                                                   '<p>To modify the payload for the required '
                                                   'status update, you should change up to 4 '
                                                   'properties. "status", "subStatus", '
                                                   '"assignedTo", and "comment" only on the '
                                                   'affected asset you want the update for.</p>\n'
                                                   "<p>If the most recent status update doesn't "
                                                   'have a "comment", this property will not show '
                                                   'on the affected asset and it will need to be '
                                                   'added.</p>\n'
                                                   '<p>Finding object payload</p>\n'
                                                   '<p>| → "affected_assets"</p>\n'
                                                   '<p>| | → Affected asset object</p>\n'
                                                   '<p>| | | → "status", "subStatus", '
                                                   '"assignedTo", and "comment"</p>\n',
                                    'folder_path': ['Affected Assets'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'create_affected_asset_status_update',
                                    'name': 'Create Affected Asset Status',
                                    'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status/update'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '',
                                    'folder_path': ['Affected Assets'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_create_affected_asset_status_updates',
                                    'name': 'Bulk Create Affected Asset Status',
                                    'path': '/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/status'}]},
 'analytics': {'display_name': 'Analytics',
               'endpoints': [{'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p><strong>Rate Limits</strong>: Due to how heavy '
                                             'this request is on the DB we have enable rate '
                                             'limiting. You can make 1 request per 5 '
                                             'seconds.</p>\n',
                              'folder_path': ['Analytics', 'Findings'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'retrieve_analytics',
                              'name': 'Retrieve Analytics',
                              'path': '/api/v1/clients/analytics'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p><strong>Rate Limits</strong>: Due to how heavy '
                                             'this request is on the DB we have enable rate '
                                             'limiting. You can make 1 request per 5 seconds.</p>\n'
                                             '<p>This request retrieves <strong>analytics on '
                                             'findings and reports per client,</strong> providing '
                                             'a total count of per client and total count by '
                                             'severity.</p>\n',
                              'folder_path': ['Analytics', 'Findings'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'retrieve_analytics_findings',
                              'name': 'Retrieve Analytics Findings',
                              'path': '/api/v1/clients/analytics/findings'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>This request retrieves <strong>analytics on '
                                             'findings based on the date of finding</strong> per '
                                             'client, providing a total count of findings per '
                                             'client and total count by severity. The query '
                                             'defaults to 30 days but can be set to 60 and 90 '
                                             'days.</p>\n',
                              'folder_path': ['Analytics', 'Findings'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'retreive_analytics_findings_aging',
                              'name': 'Retreive Analytics Findings Aging',
                              'path': '/api/v1/clients/analytics/findings/aging'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>StartFragment</p>\n'
                                             '<p>This request retrieves <strong>finding '
                                             'analytics</strong> based on filters.</p>\n'
                                             '<p>Payload params:</p>\n'
                                             '<div class="click-to-expand-wrapper '
                                             'is-table-wrapper"><table>\n'
                                             '<thead>\n'
                                             '<tr>\n'
                                             '<th><strong>Parameter</strong></th>\n'
                                             '<th><strong>Required (y/n)</strong></th>\n'
                                             '<th><strong>Type</strong></th>\n'
                                             '</tr>\n'
                                             '</thead>\n'
                                             '<tbody>\n'
                                             '<tr>\n'
                                             '<td>clients</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[number]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>clientTags</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>assetTags</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>reports</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[number]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>reportTags</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>findingTags</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>order</td>\n'
                                             '<td>y</td>\n'
                                             '<td>array[string] where valid strings are in the '
                                             'list: "reportTags", "clients", "reportTags", '
                                             '"findingTags", "reports", "assetTags", "assignees", '
                                             '"assetPorts", "operatingSystem", "dataOwner", '
                                             '"systemOwner", "physicalLocation", "cveIDs", '
                                             '"cweIDs"</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>assetPagination</td>\n'
                                             '<td>n</td>\n'
                                             '<td>see table below</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>runbooks</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>methodologies</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>engagements</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>engagementTags</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>tactics</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>assignees</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>assetPorts</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>operatingSystem</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>dataOwner</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>systemOwner</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>physicalLocation</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>cveIDs</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>cweIDs</td>\n'
                                             '<td>n</td>\n'
                                             '<td>array[string]</td>\n'
                                             '</tr>\n'
                                             '</tbody>\n'
                                             '</table>\n'
                                             '</div><p>EndFragment</p>\n'
                                             '<p>assetPagination</p>\n'
                                             '<div class="click-to-expand-wrapper '
                                             'is-table-wrapper"><table>\n'
                                             '<thead>\n'
                                             '<tr>\n'
                                             '<th><strong>Parameter</strong></th>\n'
                                             '<th><strong>Required</strong></th>\n'
                                             '<th><strong>Type</strong></th>\n'
                                             '</tr>\n'
                                             '</thead>\n'
                                             '<tbody>\n'
                                             '<tr>\n'
                                             '<td>limit</td>\n'
                                             '<td>y</td>\n'
                                             '<td>number</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>offset</td>\n'
                                             '<td>y</td>\n'
                                             '<td>number</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>total</td>\n'
                                             '<td>y</td>\n'
                                             '<td>number</td>\n'
                                             '</tr>\n'
                                             '<tr>\n'
                                             '<td>search</td>\n'
                                             '<td>y</td>\n'
                                             '<td>string: allows empty string</td>\n'
                                             '</tr>\n'
                                             '</tbody>\n'
                                             '</table>\n'
                                             '</div>',
                              'folder_path': ['Analytics', 'Findings'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'get_finding_analytics_bootstrap',
                              'name': 'Get Finding Analytics Bootstrap',
                              'path': '/api/v2/findingAnalytics/bootstrap'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p><strong>Rate Limits</strong>: Due to how heavy '
                                             'this request is on the DB we have enable rate '
                                             'limiting. You can make 1 request per 5 seconds.</p>\n'
                                             '<p>This request <strong>retrieves information about '
                                             'assets</strong> stored in the '
                                             '<strong>Clients</strong> module.</p>\n'
                                             '<p>POST:</p>\n'
                                             '<ul>\n'
                                             '<li><p>clients: int[]</p>\n'
                                             '</li>\n'
                                             '<li><p>type: string[]</p>\n'
                                             '</li>\n'
                                             '<li><p>criticality: string[]</p>\n'
                                             '</li>\n'
                                             '<li><p>data_owner: string</p>\n'
                                             '</li>\n'
                                             '<li><p>physical_location: string</p>\n'
                                             '</li>\n'
                                             '<li><p>system_owner: string</p>\n'
                                             '</li>\n'
                                             '<li><p>tags: { assets: string[] }</p>\n'
                                             '</li>\n'
                                             '</ul>\n',
                              'folder_path': ['Analytics', 'Assets'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'retrieve_analytics_assets',
                              'name': 'Retrieve Analytics Assets',
                              'path': '/api/v2/clients/analytics/assets/overview'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [('limit', '10'), ('offset', '0')],
                              'description': '<p>This request <strong>retrieves information about '
                                             'assets</strong> stored under clients and provides '
                                             'the ability to filter and limit the data set '
                                             'returned.</p>\n'
                                             '<p>POST:</p>\n'
                                             '<ul>\n'
                                             '<li>clients: int[]</li>\n'
                                             '<li>type: string[]</li>\n'
                                             '<li>criticality: string[]</li>\n'
                                             '<li>data_owner: string</li>\n'
                                             '<li>physical_location: string</li>\n'
                                             '<li>system_owner: string</li>\n'
                                             '<li>tags: { assets: string[] }</li>\n'
                                             '</ul>\n'
                                             '<p>GET:</p>\n'
                                             '<ul>\n'
                                             '<li>limit: int (default 10)</li>\n'
                                             '<li>offset: int (default 0)</li>\n'
                                             '</ul>\n',
                              'folder_path': ['Analytics', 'Assets'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'retrieve_analytics_assets_with_filter',
                              'name': 'Retrieve Analytics Assets with Filter',
                              'path': '/api/v2/clients/analytics/assets'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>POST:</p>\n'
                                             '<ul>\n'
                                             '<li>clients: int[]</li>\n'
                                             '<li>reports: int[]</li>\n'
                                             '<li>severity: string[]</li>\n'
                                             '<li>tags: { findings: string[], reports: string[] '
                                             '}</li>\n'
                                             '</ul>\n',
                              'folder_path': ['Analytics', 'Trends'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'analytics_trends_opened_closed',
                              'name': 'Analytics - Trends - Opened Closed',
                              'path': '/api/v2/clients/analytics/trends/opened-closed'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>POST:</p>\n'
                                             '<ul>\n'
                                             '<li>clients: int[]</li>\n'
                                             '<li>reports: int[]</li>\n'
                                             '<li>severity: string[]</li>\n'
                                             '<li>tags: { findings: string[], reports: string[] '
                                             '}</li>\n'
                                             '</ul>\n',
                              'folder_path': ['Analytics', 'Trends'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'analytics_trends_from_creation_to_close',
                              'name': 'Analytics - Trends - From creation to close',
                              'path': '/api/v2/clients/analytics/trends/from-creation-to-close'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>POST:</p>\n'
                                             '<ul>\n'
                                             '<li>clients: int[]</li>\n'
                                             '<li>reports: int[]</li>\n'
                                             '<li>severity: string[]</li>\n'
                                             '<li>tags: { findings: string[], reports: string[] '
                                             '}</li>\n'
                                             '</ul>\n',
                              'folder_path': ['Analytics', 'Trends'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'analytics_trends_age_of_open_findings',
                              'name': 'Analytics - Trends - Age of open findings',
                              'path': '/api/v2/clients/analytics/trends/age-of-open-findings'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Analytics', 'Trends'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'analytics_trends_slas',
                              'name': 'Analytics - Trends - SLAs',
                              'path': '/api/v2/sla/analytics/mean-time'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Analytics', 'Trends'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'analytics_trends_sla_findings',
                              'name': 'Analytics - Trends - SLA Findings',
                              'path': '/api/v2/sla/analytics/findings'}]},
 'assessments': {'display_name': 'Assessments',
                 'endpoints': [{'aliases': [],
                                'body_mode': 'none',
                                'default_params': [('limit', '50'), ('offset', '0')],
                                'description': '<p>This request <strong>retrieves</strong> all '
                                               'questions that exist for a specific '
                                               'questionnaire.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Questions'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'list_questions',
                                'name': 'List Questions',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/questions'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>retrieves</strong> '
                                               '<strong>a specific</strong> question from a '
                                               'specific questionnaire.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Questions'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_question',
                                'name': 'Get Question',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>creates a '
                                               'question</strong> for a specific '
                                               'questionnaire.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Questions'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'create_question',
                                'name': 'Create Question',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/questions'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>updates</strong> a '
                                               'questions that exists for a specific '
                                               'questionnaire.</p>\n'
                                               '<p>{<br />"answer_type": "multiSelect",<br '
                                               '/>"category": "Protection",<br '
                                               '/>"recommendations": "recommendation",<br '
                                               '/>"references": "refenreces",<br />"score": {<br '
                                               '/>"calculation": "ccv",<br />"value": ""<br '
                                               '/>},<br />"severity": "High",<br />"text": '
                                               '"xxxx",<br />"title": "Yes (Fail) / No (Pass) '
                                               'II",<br />"order": 2,<br />"tags": '
                                               '["questionnaire_xyz", "asset-tag", "c", '
                                               '"questionnaire_abc", "in"],<br '
                                               '/>"multi_choice_answers": [<br />{"answer": '
                                               '"test"},<br />{"answer": "test 1"}<br />],<br '
                                               '/>"write_up": "template_10377836",<br '
                                               '/>"custom_fields": [{<br />"key": "1",<br '
                                               '/>"label": "Custom Field",<br />"value": "foo"<br '
                                               '/>},{<br />"key": "2",<br />"label": "Custom Field '
                                               '2",<br />"value": "bar"<br />}]<br />}</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Questions'],
                                'graphql_query': None,
                                'method': 'PUT',
                                'method_name': 'update_question',
                                'name': 'Update Question',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>changes the order</strong> '
                                               'of a specific question for a specific '
                                               'questionnaire.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Questions'],
                                'graphql_query': None,
                                'method': 'PUT',
                                'method_name': 'change_question_order',
                                'name': 'Change Question Order',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}/order'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>deletes</strong> a '
                                               'specific question for a specific '
                                               'questionnaire.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Questions'],
                                'graphql_query': None,
                                'method': 'DELETE',
                                'method_name': 'delete_question',
                                'name': 'Delete Question',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/questions/{questionId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>retrieves</strong> '
                                               '<strong>all answer types</strong> that exist for a '
                                               'client.</p>\n'
                                               '<p>Can use the <code>clientId</code> of '
                                               '<code>0</code> to return all answer types in the '
                                               'tenant.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Answer Types'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'list_answer_types',
                                'name': 'List Answer Types',
                                'path': '/api/v2/tenant/{tenantId}/client/{clientId}/answertypes'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>retrieves a specific '
                                               'answer type</strong> using '
                                               '<code>answerTypeId</code>.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Answer Types'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_answer_type',
                                'name': 'Get Answer Type',
                                'path': '/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>updates a specific answer '
                                               'type</strong> for a specific client using '
                                               '<code>answerTypeId</code>.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Answer Types'],
                                'graphql_query': None,
                                'method': 'PUT',
                                'method_name': 'update_answer_type',
                                'name': 'Update Answer Type',
                                'path': '/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>creates an answer</strong> '
                                               'for a specific client.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Answer Types'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'create_answer_type',
                                'name': 'Create Answer Type',
                                'path': '/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/create'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>deletes a specific answer '
                                               'type</strong> for a specific client using '
                                               '<code>answerTypeId</code>.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires', 'Answer Types'],
                                'graphql_query': None,
                                'method': 'DELETE',
                                'method_name': 'delete_answer_type',
                                'name': 'Delete Answer Type',
                                'path': '/api/v2/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request retrieves <strong>all</strong> '
                                               'assessments for a tenant.</p>\n'
                                               '<p>The <code>instanceUrl</code> and '
                                               '<code>tenantId</code> is needed to execute the '
                                               'call.</p>\n'
                                               '<p>Below is returned on a successful call:</p>\n'
                                               '<div class="click-to-expand-wrapper '
                                               'is-table-wrapper"><table>\n'
                                               '<thead>\n'
                                               '<tr>\n'
                                               '<th><strong>parameter</strong></th>\n'
                                               '<th><strong>definition</strong></th>\n'
                                               '<th><strong>example value</strong></th>\n'
                                               '</tr>\n'
                                               '</thead>\n'
                                               '<tbody>\n'
                                               '<tr>\n'
                                               '<td>questionniare_id</td>\n'
                                               '<td>ID of assessment</td>\n'
                                               '<td>1345</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>assessment_title</td>\n'
                                               '<td>title of assessment</td>\n'
                                               '<td>CIS Control 12: Boundary Defense</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>framework</td>\n'
                                               '<td>framework that questionnaire was assessed '
                                               'against</td>\n'
                                               '<td>cis20</td>\n'
                                               '</tr>\n'
                                               '</tbody>\n'
                                               '</table>\n'
                                               '</div>',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'list_questionnaires',
                                'name': 'List Questionnaires',
                                'path': '/api/v1/tenant/{tenantId}/assessments'},
                               {'aliases': [],
                                'body_mode': 'formdata',
                                'default_params': [],
                                'description': '<p>This request retrieves a specific questionnaire '
                                               'from the <strong>Assessments</strong> '
                                               'module.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_questionnaire',
                                'name': 'Get Questionnaire',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>creates</strong> a '
                                               'questionnaire to be stored in the '
                                               '<strong>Assessments</strong> module.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'create_questionnaire',
                                'name': 'Create Questionnaire',
                                'path': '/api/v2/assessments/questionnaires'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>updates</strong> '
                                               'information for a specific questionnaire in the '
                                               '<strong>Assessments</strong> module.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'PUT',
                                'method_name': 'update_questionnaire',
                                'name': 'Update Questionnaire',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>removes</strong> an '
                                               'assessment from a tenant.</p>\n'
                                               '<p>The <code>instanceUrl</code>, '
                                               '<code>tenantId</code>, and '
                                               '<code>questionnaireId</code> is needed to execute '
                                               'the call.</p>\n'
                                               '<p>When successful, the following parameters will '
                                               'be returned:</p>\n'
                                               '<div class="click-to-expand-wrapper '
                                               'is-table-wrapper"><table>\n'
                                               '<thead>\n'
                                               '<tr>\n'
                                               '<th><strong>parameter</strong></th>\n'
                                               '<th><strong>definition</strong></th>\n'
                                               '<th><strong>example value</strong></th>\n'
                                               '</tr>\n'
                                               '</thead>\n'
                                               '<tbody>\n'
                                               '<tr>\n'
                                               '<td>status</td>\n'
                                               '<td>validation of delete request</td>\n'
                                               '<td>success</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>message</td>\n'
                                               '<td>explanation of request</td>\n'
                                               '<td>Questionnaire 0 deleted successfully!</td>\n'
                                               '</tr>\n'
                                               '</tbody>\n'
                                               '</table>\n'
                                               '</div>',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'DELETE',
                                'method_name': 'delete_questionnaire',
                                'name': 'Delete Questionnaire',
                                'path': '/api/v1/tenant/{tenantId}/assessment/{questionnaireId}'},
                               {'aliases': [],
                                'body_mode': 'formdata',
                                'default_params': [],
                                'description': '<p>This request <strong>exports</strong> a '
                                               'specific questionnaire from the '
                                               '<strong>Assessments</strong> module.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'export_questionnaire',
                                'name': 'Export Questionnaire',
                                'path': '/api/v2/assessments/questionnaires/{questionnaireId}/export'},
                               {'aliases': [],
                                'body_mode': 'formdata',
                                'default_params': [],
                                'description': '<p>This request imports a questionnaire to the '
                                               '<strong>Assessments</strong> module.</p>\n',
                                'folder_path': ['Assessments', 'Questionnaires'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'import_questionnaire',
                                'name': 'Import Questionnaire',
                                'path': '/api/v2/import/questionnaire'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [('limit', '10'),
                                                   ('offset', '0'),
                                                   ('order', 'ascend'),
                                                   ('sort', 'ALL_DESCEND')],
                                'description': '<p>This request <strong>retrieves a list of '
                                               'assessments</strong> for a specific tenant with '
                                               'the ability to sort and filter results.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'list_tenant_assessments',
                                'name': 'List Tenant Assessments',
                                'path': '/api/v2/tenants/{tenantId}/assessments'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request retrieves a list of '
                                               '<strong>all</strong> assessments for <strong>a '
                                               'specific client</strong> within a tenant.</p>\n'
                                               '<p>The <code>instanceUrl</code> , '
                                               '<code>tenantId</code> and <code>clientId</code> is '
                                               'needed to execute the call.</p>\n'
                                               '<p>Below is returned on a successful call:</p>\n'
                                               '<div class="click-to-expand-wrapper '
                                               'is-table-wrapper"><table>\n'
                                               '<thead>\n'
                                               '<tr>\n'
                                               '<th><strong>parameter</strong></th>\n'
                                               '<th><strong>definition</strong></th>\n'
                                               '<th><strong>example value</strong></th>\n'
                                               '</tr>\n'
                                               '</thead>\n'
                                               '<tbody>\n'
                                               '<tr>\n'
                                               '<td>client_name</td>\n'
                                               '<td>name of client</td>\n'
                                               '<td>Karbo Industries</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>tenant_id</td>\n'
                                               '<td>ID of tenant</td>\n'
                                               '<td>0</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>assess_ID</td>\n'
                                               '<td>assessment ID</td>\n'
                                               '<td>3098</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>questionniare_id</td>\n'
                                               '<td>ID of questionnaire</td>\n'
                                               '<td>1345</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>assessment_title</td>\n'
                                               '<td>title of assessment</td>\n'
                                               '<td>CIS Control 12: Boundary Defense</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>doc_type</td>\n'
                                               '<td>document type</td>\n'
                                               '<td>assessment</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>assessment_date</td>\n'
                                               '<td>date assessment was created</td>\n'
                                               '<td>1652733751471</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>saved_at</td>\n'
                                               '<td>date assessment was last saved</td>\n'
                                               '<td>1652733751471</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>last_updated_by</td>\n'
                                               '<td>user who saved assessment</td>\n'
                                               '<td>0</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>has_reviewers</td>\n'
                                               '<td>identifies if assessment has reviewers or '
                                               'not</td>\n'
                                               '<td>false</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>reviewers</td>\n'
                                               '<td>if assessment has reviewers, they will be '
                                               'listed here</td>\n'
                                               '<td>[]</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>all_approved</td>\n'
                                               '<td>if applicable, identifies if assessment has '
                                               'been approved by all reviewers</td>\n'
                                               '<td>false</td>\n'
                                               '</tr>\n'
                                               '</tbody>\n'
                                               '</table>\n'
                                               '</div>',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'list_client_assessments',
                                'name': 'List Client Assessments',
                                'path': '/api/v1/tenant/{tenantId}/client/{clientId}/assessments'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [('offset', '0'),
                                                   ('limit', '10'),
                                                   ('sort', '0'),
                                                   ('order', 'ascend')],
                                'description': '',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'list_client_assessments_filtered',
                                'name': 'List Client Assessments (Filtered)',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request retrieves a list of <strong>a '
                                               'specific</strong> assessment for <strong>a '
                                               'specific client</strong> within a tenant.</p>\n'
                                               '<p>The <code>instanceUrl</code> , '
                                               '<code>tenantId</code> , <code>clientId</code>, and '
                                               '<code>assessmentID</code> is needed to execute the '
                                               'call.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_client_assessment_with_questions_and_answers',
                                'name': 'Get Client Assessment (with questions and answers)',
                                'path': '/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>returns the data for a '
                                               'specific assessment</strong> started for <strong>a '
                                               'specific client</strong>.</p>\n'
                                               '<p>You can determine if the assessment is '
                                               '<strong>In Progress</strong> or '
                                               '<strong>Completed</strong> with the addition of '
                                               'the <code>completed_at</code> field in the '
                                               'response.</p>\n'
                                               '<ul>\n'
                                               '<li>If this field is included in the response, the '
                                               'assessment was <strong>completed</strong> at the '
                                               'time value given.</li>\n'
                                               '<li>If the field is not included in the response, '
                                               'the assessment is <strong>In '
                                               'Progress</strong>.</li>\n'
                                               '</ul>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_client_assessment',
                                'name': 'Get Client Assessment',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_assessment_by_cuid',
                                'name': 'Get Assessment by CUID',
                                'path': '/api/v2/assessments/{assessmentCuid}'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [('offset', '0'),
                                                   ('limit', '3'),
                                                   ('order', 'ascend')],
                                'description': '<p>This request <strong>retrieves questions for a '
                                               'specific assessment</strong> for <strong>a '
                                               'specific client</strong> with the ability to sort '
                                               'and filter results.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_assessment_questions',
                                'name': 'Get Assessment Questions',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/questions'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [('limit', '3'),
                                                   ('offset', '0'),
                                                   ('order', 'ascend')],
                                'description': '<p>This request <strong>retrieves answers for a '
                                               'specific assessment</strong> for <strong>a '
                                               'specific client</strong> with the ability to sort '
                                               'and filter results.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_assessment_answers',
                                'name': 'Get Assessment Answers',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>updates answers</strong> '
                                               'for an assessment.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'PUT',
                                'method_name': 'update_assessment_answers',
                                'name': 'Update Assessment Answers',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request <strong>retrieves a list of '
                                               'reviewers</strong> for a an assessment.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'GET',
                                'method_name': 'get_assessment_reviewers',
                                'name': 'Get Assessment Reviewers',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/reviewers'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>creates</strong> a new '
                                               'assessment for a specific client within a '
                                               'tenant.</p>\n'
                                               '<p>The <code>instanceUrl</code> , '
                                               '<code>tenantId</code> and <code>clientId</code> is '
                                               'needed to execute the call.</p>\n'
                                               '<p><strong>NOTE:</strong> This endpoint is meant '
                                               'to create a new Client Assessment from an existing '
                                               'Questionnaire. To reopen a completed Client '
                                               'Assessment see <a '
                                               'href="https://api-docs.plextrac.com/#32db8121-7206-495c-92af-8f563eb33e7a">Copy '
                                               'Client Assessment</a></p>\n'
                                               '<p><strong>NOTE:</strong> It is recommended that '
                                               'the optional field <code>saveOnly</code> is set to '
                                               '<code>True</code>. This field detemines whether to '
                                               'just save the newly created Client Assesment or '
                                               'add all current answers in the response. If the '
                                               '<code>answers</code> field sent in the payload was '
                                               'an empty array, the answers returned will just be '
                                               'the default empty values from the Questionnaire. '
                                               'This makes the response unnecessarily long '
                                               'depending on the number of questions in the '
                                               'assessment.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'create_client_assessment',
                                'name': 'Create Client Assessment',
                                'path': '/api/v1/tenant/{tenantId}/client/{clientId}/assessment'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>updates</strong> an '
                                               'assessment.</p>\n'
                                               '<p>The <code>instanceUrl</code> , '
                                               '<code>tenantId</code>, <code>assessmentId</code> '
                                               'and <code>clientId</code> is needed to execute the '
                                               'call.</p>\n'
                                               '<p>The assessment is considered "In Progress" or '
                                               '"Completed" based the presence and value of the '
                                               '<code>completed_at</code> property. To mark an '
                                               'assessment complete, update the assessment to have '
                                               'a <code>completed_at</code> property containing a '
                                               'timestamp in milliseconds.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'PUT',
                                'method_name': 'update_client_assessment',
                                'name': 'Update Client Assessment',
                                'path': '/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'},
                               {'aliases': [],
                                'body_mode': 'none',
                                'default_params': [],
                                'description': '<p>This request will <strong>delete</strong> an '
                                               'assessment for a client.</p>\n'
                                               '<p>The <code>instanceUrl</code> , '
                                               '<code>tenantId</code>, <code>assessmentId</code> '
                                               'and <code>clientId</code> is needed to execute the '
                                               'call.</p>\n'
                                               '<p>When successful, the following parameters will '
                                               'be returned:</p>\n'
                                               '<div class="click-to-expand-wrapper '
                                               'is-table-wrapper"><table>\n'
                                               '<thead>\n'
                                               '<tr>\n'
                                               '<th><strong>parameter</strong></th>\n'
                                               '<th><strong>definition</strong></th>\n'
                                               '<th><strong>example value</strong></th>\n'
                                               '</tr>\n'
                                               '</thead>\n'
                                               '<tbody>\n'
                                               '<tr>\n'
                                               '<td>status</td>\n'
                                               '<td>status of delete call</td>\n'
                                               '<td>success</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>data</td>\n'
                                               '<td></td>\n'
                                               '<td></td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>message</td>\n'
                                               '<td>validation of delete request</td>\n'
                                               '<td>success</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>doc_id</td>\n'
                                               '<td>ID of assessment deleted</td>\n'
                                               '<td>assessment_3098_tenant_0_client_1912</td>\n'
                                               '</tr>\n'
                                               '</tbody>\n'
                                               '</table>\n'
                                               '</div>',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'DELETE',
                                'method_name': 'delete_client_assessment',
                                'name': 'Delete Client Assessment',
                                'path': '/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request will <strong>create a '
                                               'report</strong> from assessments for a '
                                               'client.</p>\n'
                                               '<p>The <code>instanceUrl</code> , '
                                               '<code>tenantId</code>, <code>assessmentId</code>, '
                                               '<code>clientId</code> and '
                                               '<code>questionnaireId</code> is needed to execute '
                                               'the call.</p>\n'
                                               '<p>Using this endpoint will not mark the '
                                               'assessment completed, but only create a report '
                                               'based on the current state of the assessment. '
                                               'Whether an assessment is completed or not is a '
                                               'property of the assessment object. It is '
                                               'determined by the presence and value of the '
                                               '<code>completed_at</code> property on the '
                                               'assessment.</p>\n'
                                               "<p>Leaving the 'answers' value blank will submit "
                                               'the answers currently on the assessment. Use other '
                                               "endpoints to change an assessment question's "
                                               'answers <strong>before</strong> using this call, '
                                               'if answers need to be modified.</p>\n'
                                               '<p>When successful, the following parameters will '
                                               'be returned:</p>\n'
                                               '<div class="click-to-expand-wrapper '
                                               'is-table-wrapper"><table>\n'
                                               '<thead>\n'
                                               '<tr>\n'
                                               '<th><strong>parameter</strong></th>\n'
                                               '<th><strong>definition</strong></th>\n'
                                               '<th><strong>example value</strong></th>\n'
                                               '</tr>\n'
                                               '</thead>\n'
                                               '<tbody>\n'
                                               '<tr>\n'
                                               '<td>status</td>\n'
                                               '<td>status of call</td>\n'
                                               '<td>success</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>data</td>\n'
                                               '<td></td>\n'
                                               '<td></td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>status</td>\n'
                                               '<td>status of call</td>\n'
                                               '<td>success</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>message</td>\n'
                                               '<td>validation of delete request</td>\n'
                                               '<td>full report created successfully</td>\n'
                                               '</tr>\n'
                                               '<tr>\n'
                                               '<td>report_id</td>\n'
                                               '<td>generated report ID</td>\n'
                                               '<td>35228</td>\n'
                                               '</tr>\n'
                                               '</tbody>\n'
                                               '</table>\n'
                                               '</div>',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'create_report_from_assessment_questionnaire',
                                'name': 'Create Report From Assessment Questionnaire',
                                'path': '/api/v1/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}/report'},
                               {'aliases': [],
                                'body_mode': 'raw',
                                'default_params': [],
                                'description': '<p>This request <strong>creates a new '
                                               'assessment</strong> from a previously completed '
                                               'assessment, copying over questions and '
                                               'answers.</p>\n',
                                'folder_path': ['Assessments', 'Client Assessments'],
                                'graphql_query': None,
                                'method': 'POST',
                                'method_name': 'copy_asessment_questionnaire',
                                'name': 'Copy Asessment Questionnaire',
                                'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy'}]},
 'assets': {'display_name': 'Assets',
            'endpoints': [{'aliases': [],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '<p>This request <strong>retrieves the list of assets '
                                          'for a tenant</strong>.</p>\n'
                                          '<p><code>pagination</code> is a required key while '
                                          '<code>sort</code> and <code>filters</code> are '
                                          'optional.</p>\n'
                                          '<p>The <code>pagination.limit</code> must be one of [5, '
                                          '10, 25, 50, 100, 1000]. The '
                                          '<code>pagination.offset</code> is the number of records '
                                          'to shift by, not the number of pages to shift by. i.e. '
                                          'offset 2, limit 10 gives you records 2-12 not '
                                          '20-30</p>\n'
                                          '<p>The following values can be used in the '
                                          '<code>sort.by</code> and <code>filters.by</code> '
                                          'field:</p>\n'
                                          '<ul>\n'
                                          '<li>searchTerm</li>\n'
                                          '<li>client_id</li>\n'
                                          '<li>assetCriticality</li>\n'
                                          '<li>tags</li>\n'
                                          '<li>type</li>\n'
                                          '<li>pci_status</li>\n'
                                          '<li>system_owner</li>\n'
                                          '<li>data_owner</li>\n'
                                          '</ul>\n'
                                          '<p>The following values can be used in the '
                                          '<code>sort.order</code> field:</p>\n'
                                          '<ul>\n'
                                          '<li>ASC</li>\n'
                                          '<li>DESC</li>\n'
                                          '</ul>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'POST',
                           'method_name': 'get_tenant_assets',
                           'name': 'Get Tenant Assets',
                           'path': '/api/v2/tenant/assets'},
                          {'aliases': [],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '<p>This request <strong>retrieves the list of assets '
                                          'for a specific client</strong>.</p>\n'
                                          '<p><code>pagination</code> is a required key while '
                                          '<code>sort</code> and <code>filters</code> are '
                                          'optional.</p>\n'
                                          '<p>The <code>pagination.limit</code> must be one of [5, '
                                          '10, 25, 50, 100]. The <code>pagination.offset</code> is '
                                          'the number of records to shift by, not the number of '
                                          'pages to shift by. i.e. offset 2, limit 10 gives you '
                                          'records 2-12 not 20-30</p>\n'
                                          '<p>The following values can be used in the '
                                          '<code>sort.by</code> and <code>filters.by</code> '
                                          'field:</p>\n'
                                          '<ul>\n'
                                          '<li>asset</li>\n'
                                          '<li>tags</li>\n'
                                          '</ul>\n'
                                          '<p>The following values can be used in the '
                                          '<code>sort.order</code> field:</p>\n'
                                          '<ul>\n'
                                          '<li>ASC</li>\n'
                                          '<li>DESC</li>\n'
                                          '</ul>\n'
                                          '<p><strong>Note</strong>: To filter by assets without '
                                          'any tags, use the filter obj</p>\n'
                                          '<p>{ "by": "tags", "value": ["none"] }</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'POST',
                           'method_name': 'get_assets_by_client',
                           'name': 'Get Assets by Client',
                           'path': '/api/v2/clients/{clientId}/assets'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>DEPRECATED will be removed 12/03/2024</p>\n'
                                          '<p>See <a '
                                          'href="https://api-docs.plextrac.com/#47b8f7ee-84f6-48c6-81e9-f3eeae4edb70">Get '
                                          'Tenant Assets</a> or <a '
                                          'href="https://api-docs.plextrac.com/#2c9acc54-4481-443e-9246-8ed0b452f697">List '
                                          'Report Assets</a> for replacement. See this <a '
                                          'href="https://docs.plextrac.com/plextrac-documentation/api-documentation/api-change-policy/api-change-log#release-2.12-december-3-2024">API '
                                          'Change Log</a> for more details.</p>\n'
                                          '<p>This request <strong>retrieves a list of all '
                                          'assets</strong> for a specific client.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'list_client_assets',
                           'name': 'List Client Assets',
                           'path': '/api/v1/client/{clientId}/assets'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>This request <strong>retrieves a list of assets for '
                                          'a specific report.</strong></p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'list_report_assets',
                           'name': 'List Report Assets',
                           'path': '/api/v2/clients/{clientId}/reports/{reportId}/assets'},
                          {'aliases': ['get'],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>This request <strong>retrieves a specific '
                                          'asset</strong> for a specific client.</p>\n'
                                          '<p>See our docs on the <a '
                                          'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object">Asset '
                                          'Object</a> structure for more details on the '
                                          'response.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'get_asset',
                           'name': 'Get Asset',
                           'path': '/api/v1/client/{clientId}/asset/{assetId}'},
                          {'aliases': ['create'],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '<p>This request <strong>creates an asset</strong> for a '
                                          'client.</p>\n'
                                          '<p>Currently an endpoint for creating an asset does not '
                                          'exist, use this endpoint with an ID value of "0" to '
                                          'have a new unique asset ID created.</p>\n'
                                          '<p>See our docs on the <a '
                                          'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object">Asset '
                                          'Object</a> structure for more details on possible '
                                          'keys.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'PUT',
                           'method_name': 'create_asset',
                           'name': 'Create Asset',
                           'path': '/api/v1/client/{clientId}/asset/0'},
                          {'aliases': ['update'],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '<p>This request <strong>updates a specific '
                                          'asset</strong> for a client.</p>\n'
                                          '<p>See ou rdocs on the <a '
                                          'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object">Asset '
                                          'Object</a> structure for more details on possible '
                                          'keys.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'PUT',
                           'method_name': 'update_asset',
                           'name': 'Update Asset',
                           'path': '/api/v1/client/{clientId}/asset/{assetId}'},
                          {'aliases': ['delete'],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>This request <strong>deletes a specific '
                                          'asset</strong> for a client.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'DELETE',
                           'method_name': 'delete_asset',
                           'name': 'Delete Asset',
                           'path': '/api/v1/client/{clientId}/asset/{assetId}'},
                          {'aliases': [],
                           'body_mode': 'formdata',
                           'default_params': [],
                           'description': '<p>This request imports assets from an outside tool '
                                          'into PlexTrac for a specific client.</p>\n'
                                          '<p>The source must be from the supported list '
                                          'below:</p>\n'
                                          '<p>Python Parsers (Legacy)</p>\n'
                                          '<ul>\n'
                                          '<li><p>nmap</p>\n'
                                          '</li>\n'
                                          '<li><p>csv</p>\n'
                                          '</li>\n'
                                          '</ul>\n'
                                          '<p>Type Script Parsers</p>\n'
                                          '<p>These parser have the same functionality to the '
                                          'legacy ones, they have just been ported over to a more '
                                          "stable implmentaion on a dedicated worker thread. It's "
                                          'recommended to use these over the legacy parsers.</p>\n'
                                          '<ul>\n'
                                          '<li><p>nmap-xml</p>\n'
                                          '</li>\n'
                                          '<li><p>nmap-csv</p>\n'
                                          '</li>\n'
                                          '</ul>\n'
                                          '<p>Includes support for a csv. Must use the schema '
                                          'described here:</p>\n'
                                          '<p><a '
                                          'href="https://docs.plextrac.com/plextrac-documentation/product-documentation/clients/adding-assets-in-clients">Adding '
                                          'Assets in Clients</a></p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'POST',
                           'method_name': 'import_client_assets',
                           'name': 'Import Client Assets v2',
                           'path': '/api/v2/client/{clientId}/assets/import/{source}'},
                          {'aliases': [],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '<p>This requests deletes the Client Assets sent in the '
                                          'payload.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'POST',
                           'method_name': 'bulk_delete_client_assets',
                           'name': 'Bulk Delete Client Assets',
                           'path': '/api/v1/client/{clientId}/bulk/assets/delete'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>Retrieve all Evidence on an Affected Asset.</p>\n',
                           'folder_path': ['Assets'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'get_scanner_output',
                           'name': 'Get Scanner Output',
                           'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput'}]},
 'authentication': {'display_name': 'Authentication',
                    'endpoints': [{'aliases': [],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>For more info visit: <a '
                                                  'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview#getting-started">https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview#getting-started</a></p>\n'
                                                  '<p>This request <strong>authenticates a user '
                                                  'via a username and password</strong>. Below is '
                                                  'a list of information needed to fulfil the '
                                                  'request.</p>\n'
                                                  '<div class="click-to-expand-wrapper '
                                                  'is-table-wrapper"><table>\n'
                                                  '<thead>\n'
                                                  '<tr>\n'
                                                  '<th><strong>parameter</strong></th>\n'
                                                  '<th><strong>definition</strong></th>\n'
                                                  '<th><strong>example value</strong></th>\n'
                                                  '</tr>\n'
                                                  '</thead>\n'
                                                  '<tbody>\n'
                                                  '<tr>\n'
                                                  '<td>instanceUrl</td>\n'
                                                  '<td>url of the Plextrac instance</td>\n'
                                                  '<td>example.plextrac.com</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>username</td>\n'
                                                  '<td>email address</td>\n'
                                                  '<td><a '
                                                  'href="mailto:joepentester@plextrac.com">joepentester@plextrac.com</a></td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>password</td>\n'
                                                  '<td>password value</td>\n'
                                                  '<td>1#$$35gg2</td>\n'
                                                  '</tr>\n'
                                                  '</tbody>\n'
                                                  '</table>\n'
                                                  '</div><p>When successful, the following '
                                                  'parameters will be returned:</p>\n'
                                                  '<div class="click-to-expand-wrapper '
                                                  'is-table-wrapper"><table>\n'
                                                  '<thead>\n'
                                                  '<tr>\n'
                                                  '<th><strong>parameter</strong></th>\n'
                                                  '<th><strong>definition</strong></th>\n'
                                                  '<th><strong>example value</strong></th>\n'
                                                  '</tr>\n'
                                                  '</thead>\n'
                                                  '<tbody>\n'
                                                  '<tr>\n'
                                                  '<td>status</td>\n'
                                                  '<td>measurement of the authentication '
                                                  'request</td>\n'
                                                  '<td>success</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>tenant_id</td>\n'
                                                  '<td>number that defines the PlexTrac '
                                                  'tenant</td>\n'
                                                  '<td>0</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>cookie</td>\n'
                                                  '<td>value stored in browser and attached to '
                                                  'every future request and response made to '
                                                  'client and server to validate access</td>\n'
                                                  '<td>eyJhbGci...</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>token</td>\n'
                                                  "<td>value that uniquely identifies the user's "
                                                  'session</td>\n'
                                                  '<td>eyJhbGci...</td>\n'
                                                  '</tr>\n'
                                                  '</tbody>\n'
                                                  '</table>\n'
                                                  '</div>',
                                   'folder_path': ['Authentication', 'Authenticate'],
                                   'graphql_query': None,
                                   'method': 'POST',
                                   'method_name': 'authentication',
                                   'name': 'Authentication',
                                   'path': '/api/v1/authenticate'},
                                  {'aliases': [],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>This request <strong>validates access via '
                                                  'multifactor authentication (MFA)</strong> and '
                                                  'requires additional verification. Below is a '
                                                  'list of information needed to fulfil the '
                                                  'request.</p>\n'
                                                  '<div class="click-to-expand-wrapper '
                                                  'is-table-wrapper"><table>\n'
                                                  '<thead>\n'
                                                  '<tr>\n'
                                                  '<th><strong>parameter</strong></th>\n'
                                                  '<th><strong>definition</strong></th>\n'
                                                  '<th><strong>example value</strong></th>\n'
                                                  '</tr>\n'
                                                  '</thead>\n'
                                                  '<tbody>\n'
                                                  '<tr>\n'
                                                  '<td>instanceUrl</td>\n'
                                                  '<td>url of the Plextrac instance</td>\n'
                                                  '<td>example.plextrac.com</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>code</td>\n'
                                                  '<td>MFA token value</td>\n'
                                                  '<td>auto-gen</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>token</td>\n'
                                                  '<td>6-digit MFA code</td>\n'
                                                  '<td>524889</td>\n'
                                                  '</tr>\n'
                                                  '</tbody>\n'
                                                  '</table>\n'
                                                  '</div><p>When successful, the following '
                                                  'parameters will be returned:</p>\n'
                                                  '<div class="click-to-expand-wrapper '
                                                  'is-table-wrapper"><table>\n'
                                                  '<thead>\n'
                                                  '<tr>\n'
                                                  '<th><strong>parameter</strong></th>\n'
                                                  '<th><strong>definition</strong></th>\n'
                                                  '<th><strong>example value</strong></th>\n'
                                                  '</tr>\n'
                                                  '</thead>\n'
                                                  '<tbody>\n'
                                                  '<tr>\n'
                                                  '<td>status</td>\n'
                                                  '<td>measurement of the authentication '
                                                  'request</td>\n'
                                                  '<td>success</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>tenant_id</td>\n'
                                                  '<td>number that defines the PlexTrac '
                                                  'tenant</td>\n'
                                                  '<td>0</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>cookie</td>\n'
                                                  '<td>value stored in browser and attached to '
                                                  'every future request and response made to '
                                                  'client and server to validate access</td>\n'
                                                  '<td>eyJhbGci...</td>\n'
                                                  '</tr>\n'
                                                  '<tr>\n'
                                                  '<td>token</td>\n'
                                                  "<td>value that uniquely identifies the user's "
                                                  'session</td>\n'
                                                  '<td>eyJhbGci...</td>\n'
                                                  '</tr>\n'
                                                  '</tbody>\n'
                                                  '</table>\n'
                                                  '</div>',
                                   'folder_path': ['Authentication', 'Authenticate'],
                                   'graphql_query': None,
                                   'method': 'POST',
                                   'method_name': 'multi_factor_authentication',
                                   'name': 'Multi-Factor Authentication',
                                   'path': '/api/v1/authenticate/mfa'},
                                  {'aliases': [],
                                   'body_mode': 'none',
                                   'default_params': [],
                                   'description': '<p>This endpoint is used to refresh the '
                                                  'authentication token.</p>\n'
                                                  '<p>Call this endpoint with no params or body '
                                                  'and it will use the existing authentication '
                                                  'header token sent (instead of the '
                                                  'username/password/MFA) to generate a new token. '
                                                  'This new token is the start of a new 15 minute '
                                                  'authentication session.</p>\n'
                                                  '<h4 id="response">Response</h4>\n'
                                                  '<p>The response is the same as the <a '
                                                  'href="https://api-docs.plextrac.com/#5c8b0f53-9ef9-4df3-bfcd-0539b7b06e28">Authentication '
                                                  '</a> endpoint response.</p>\n'
                                                  '<ul>\n'
                                                  '<li><p><strong>status</strong> (string): The '
                                                  'status of the token refresh.</p>\n'
                                                  '</li>\n'
                                                  '<li><p><strong>tenant_id</strong> (integer): '
                                                  'The ID of the tenant.</p>\n'
                                                  '</li>\n'
                                                  '<li><p><strong>token</strong> (string): The new '
                                                  'authentication token.</p>\n'
                                                  '</li>\n'
                                                  '<li><p><strong>cookie</strong> (string): The '
                                                  'cookie for the refreshed token.</p>\n'
                                                  '</li>\n'
                                                  '</ul>\n',
                                   'folder_path': ['Authentication', 'Authenticate'],
                                   'graphql_query': None,
                                   'method': 'PUT',
                                   'method_name': 'refresh_token',
                                   'name': 'Refresh Token',
                                   'path': '/api/v1/token/refresh'},
                                  {'aliases': [],
                                   'body_mode': 'none',
                                   'default_params': [],
                                   'description': '<p>This request <strong>generates a QR code '
                                                  'link</strong> that can be used to set up '
                                                  'multi-factor authorization (MFA).</p>\n'
                                                  '<p>NOTE: This action will override previous MFA '
                                                  'setup.</p>\n',
                                   'folder_path': ['Authentication', 'Setup MFA'],
                                   'graphql_query': None,
                                   'method': 'GET',
                                   'method_name': 'generate_qr_code',
                                   'name': 'Generate QR code',
                                   'path': '/api/v2/user/mfa/qr'},
                                  {'aliases': [],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>This request <strong>activates a QR '
                                                  'code</strong> that is used to set up '
                                                  'multi-factor authorization (MFA) by including '
                                                  'the six-digit MFA code provided by the '
                                                  'third-party authorization tool as a variable in '
                                                  'the body.</p>\n',
                                   'folder_path': ['Authentication', 'Setup MFA'],
                                   'graphql_query': None,
                                   'method': 'POST',
                                   'method_name': 'activate_mfa',
                                   'name': 'Activate MFA',
                                   'path': '/api/v2/user/mfa/qr/activate'}]},
 'clients': {'display_name': 'Clients',
             'endpoints': [{'aliases': [],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request retrieves a list of '
                                           '<strong>all</strong> <strong>users</strong> for a '
                                           'specific client.</p>\n',
                            'folder_path': ['Clients', 'Client Users'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'list_client_users',
                            'name': 'List Client Users v2',
                            'path': '/api/v2/tenants/{tenantId}/clients/{clientId}/users'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '',
                            'folder_path': ['Clients', 'Client Users'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'list_available_tenant_users',
                            'name': 'Available Tenant Users',
                            'path': '/api/v1/tenant/{tenantId}/client/{clientId}/users/available'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This endpoint allows you to assign users to a '
                                           'client within a specific tenant.</p>\n'
                                           '<h3 id="request-body">Request Body</h3>\n'
                                           '<ul>\n'
                                           '<li>The request should be sent as a JSON object with '
                                           'an array of users, where each user object contains the '
                                           'following parameters:<ul>\n'
                                           '<li><code>username</code> (string): The email of the '
                                           'user to be assigned.</li>\n'
                                           '<li><code>role</code> (string): The role to be '
                                           'assigned to the user.</li>\n'
                                           '<li><code>classificationId</code> (string): The ID of '
                                           'the classification tier to set the user to.</li>\n'
                                           '</ul>\n'
                                           '</li>\n'
                                           '</ul>\n'
                                           '<p>The <code>role</code> field must contain the RBAC '
                                           'role code. The codes for the default roles are:</p>\n'
                                           '<ul>\n'
                                           '<li><p>Administrator - <code>ADMIN</code></p>\n'
                                           '</li>\n'
                                           '<li><p>Standard User - <code>STD_USER</code></p>\n'
                                           '</li>\n'
                                           '<li><p>Analyst - <code>ANALYST</code></p>\n'
                                           '</li>\n'
                                           '</ul>\n'
                                           '<p>A custom RBAC role will have a role code created in '
                                           'the format</p>\n'
                                           '<ul>\n'
                                           '<li>Custom Role - '
                                           '<code>TENANT_0_ROLE_CUSTOM-ROLE-NAME</code></li>\n'
                                           '</ul>\n'
                                           '<h3 id="response">Response</h3>\n'
                                           '<p>Upon a successful execution, the response will have '
                                           'a status code of 200. The response body will '
                                           'include:</p>\n'
                                           '<ul>\n'
                                           '<li><code>status</code> (string): The status of the '
                                           'assignment.</li>\n'
                                           '<li><code>users_assigned</code> (array): An array of '
                                           'emails that have been successfully assigned.</li>\n'
                                           '<li><code>users_rejected</code> (array): An array of '
                                           'emails that were rejected during the assignment '
                                           'process.</li>\n'
                                           '</ul>\n'
                                           "<p>If an email is entered that isn't associated with a "
                                           'user, the response will not contain that email in '
                                           'either the assigned or rejected list.</p>\n',
                            'folder_path': ['Clients', 'Client Users'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'assign_users_to_client',
                            'name': 'Assign User to Client v2',
                            'path': '/api/v2/tenant/{tenantId}/client/{clientId}/user/assign'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p><strong>Known Bug:</strong> This endpoint will not '
                                           'add or update a users classification level, even if '
                                           'Classification Tiers are enabled in your '
                                           'instance.</p>\n'
                                           '<p>This request <strong>assigns a list of users to '
                                           'have a certain level of permission for a specific '
                                           'client</strong>.</p>\n'
                                           '<p>The role is the level of access a user will be '
                                           'assigned for the client being added to. This can '
                                           'differ from the default role a user is assigned.</p>\n'
                                           '<p>For example: A user can have the <em>Analyst</em> '
                                           'role assigned as the default role that will be apply '
                                           'to all clients they have access to. They can then be '
                                           'assigned the <em>Standard User</em> role for a certain '
                                           'client, adding the extra permissions when inside that '
                                           'specific client.</p>\n'
                                           '<p>The "role" field must contain the RBAC role code. '
                                           'The codes for the default roles are:</p>\n'
                                           '<p>Administrator - <code>ADMIN</code></p>\n'
                                           '<p>Standard User - <code>STD_USER</code></p>\n'
                                           '<p>Analyst - <code>ANALYST</code></p>\n'
                                           '<p>A custom RBAC role will have a role code created in '
                                           'the format</p>\n'
                                           '<p>Custom Role - '
                                           '<code>TENANT_0_ROLE_CUSTOM_ROLE</code></p>\n'
                                           '<p>The rest of the fields should match the values of '
                                           'the existing user.</p>\n',
                            'folder_path': ['Clients', 'Client Users'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'bulk_assign_users_to_client',
                            'name': 'Bulk Assign Users to Client',
                            'path': '/api/v2/tenant/{tenantId}/client/{clientId}/bulk/users/assign'},
                           {'aliases': [],
                            'body_mode': 'formdata',
                            'default_params': [],
                            'description': "<p>Revoke a user's authorization from a client</p>\n",
                            'folder_path': ['Clients', 'Client Users'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'remove_users_from_client',
                            'name': 'Remove User from Client',
                            'path': '/api/v1/tenant/{tenantId}/client/{clientId}/user/remove'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>List all clients of a given tenant</p>\n',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'list_tenant_clients',
                            'name': 'List Tenant Clients',
                            'path': '/api/v1/tenant/{tenantId}/client/list'},
                           {'aliases': ['list'],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request retrieves a list of '
                                           '<strong>all</strong> <strong>clients</strong> within a '
                                           'tenant. The body contains information on how to filter '
                                           'and sort the data to return.</p>\n'
                                           '<p>{<br />pagination: { // required object with keys '
                                           '"offset" &amp; "limit"<br />offset: 0, // required '
                                           'number, default 0<br />limit: 25, // required number '
                                           'valid [5, 25, 50, 100]<br />},<br />sort: [ // '
                                           'optional array of objects with keys "by" &amp; '
                                           '"order"<br />{<br />by: "asset", // required string<br '
                                           '/>order: "DESC", // required one of "ASC" | "DESC"<br '
                                           '/>},<br />],<br />filters: [ // optional array of '
                                           'object with keys "by" &amp; "value"<br />{<br />by: '
                                           '"asset", // required string<br />value: "ba", // '
                                           'required string allows "empty string" if filtering by '
                                           '"tags" must be array of strings<br />},<br />],<br '
                                           '/>}</p>\n',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'list_clients',
                            'name': 'List Clients',
                            'path': '/api/v2/clients'},
                           {'aliases': ['get'],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request retrieves information on a client for '
                                           'a tenant that you are <strong>authorized</strong> to '
                                           'view.</p>\n'
                                           '<p>The <code>instanceUrl</code> and '
                                           '<code>clientId</code> is needed to execute the '
                                           'call.</p>\n'
                                           '<p>A successsfull call returns the JSON object of the '
                                           'cient stored in the DB. See <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/client-object">Client '
                                           'Object</a> for deatils on how this JSON is '
                                           'structured</p>\n',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'get_client',
                            'name': 'Get Client',
                            'path': '/api/v1/client/{clientId}'},
                           {'aliases': ['create'],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request <strong>creates</strong> a new client '
                                           'within a tenant.</p>\n'
                                           '<p>The <code>instanceUrl</code> is needed to execute '
                                           'the call.</p>\n'
                                           '<p>In addition to the example below, see <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/client-object">Client '
                                           'Object</a> for details on the payload structure</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>validation of request</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>client_id</td>\n'
                                           '<td>Id of the newly created client</td>\n'
                                           '<td>1234</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>assign_message</td>\n'
                                           '<td>dictionary that summarizes which users were '
                                           'granted acces to the client. This includes the user '
                                           'issuing the request and any user in the default '
                                           'group.</td>\n'
                                           '<td></td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div><p><code>assign_message</code> dictionary '
                                           'structure</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>status of assigning users to new client</td>\n'
                                           '<td>complete</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>users_assigned</td>\n'
                                           '<td>List of user emails that were assigned to '
                                           'client</td>\n'
                                           '<td>["<a '
                                           'href="mailto:test@email.com">test@email.com</a>"]</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>users_rejected</td>\n'
                                           '<td>List of user emails that failed to get assigned to '
                                           'client</td>\n'
                                           '<td>["<a '
                                           'href="mailto:test@email.com">test@email.com</a>"]</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'create_client',
                            'name': 'Create Client',
                            'path': '/api/v1/client/create'},
                           {'aliases': ['update'],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request updates an existing client within a '
                                           'tenant.</p>\n'
                                           '<p>The <code>instanceUrl</code> and '
                                           '<code>clientId</code> is needed to execute the '
                                           'call.</p>\n'
                                           '<p>In addition to the example below, see <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/client-object">Client '
                                           'Object</a> for details on the payload structure.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>validation of request</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>message</td>\n'
                                           '<td>explanation of request</td>\n'
                                           '<td>Client updated successfully.</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'PUT',
                            'method_name': 'update_client',
                            'name': 'Update Client',
                            'path': '/api/v1/client/{clientId}'},
                           {'aliases': ['delete'],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request <strong>removes</strong> a client from '
                                           'a tenant.</p>\n'
                                           '<p>The <code>instanceUrl</code> and '
                                           '<code>clientId</code> is needed to execute the '
                                           'call.</p>\n'
                                           '<p>When successful, the following parameters will be '
                                           'returned:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>validation of delete request</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>message</td>\n'
                                           '<td>explanation of request</td>\n'
                                           '<td>client deleted successfully</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'DELETE',
                            'method_name': 'delete_client',
                            'name': 'Delete Client',
                            'path': '/api/v1/client/{clientId}'},
                           {'aliases': [],
                            'body_mode': 'formdata',
                            'default_params': [],
                            'description': '<p>This request <strong>creates</strong> a logo for a '
                                           'client. The file must be JPEG or PNG.</p>\n'
                                           '<p>The <code>instanceUrl</code> and '
                                           '<code>clientId</code> is needed to execute the '
                                           'call.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>validation of request</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>message</td>\n'
                                           '<td>further validation</td>\n'
                                           '<td>Client Logo Updated</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'add_client_logo',
                            'name': 'Add Client Logo',
                            'path': '/api/v1/client/{clientId}/logo'},
                           {'aliases': [],
                            'body_mode': 'formdata',
                            'default_params': [],
                            'description': '<p>This request <strong>removes</strong> a logo for a '
                                           'client.</p>\n'
                                           '<p>The <code>instanceUrl</code> and '
                                           '<code>clientId</code> is needed to execute the '
                                           'call.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>validation of request</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>message</td>\n'
                                           '<td>further validation</td>\n'
                                           '<td>Client Logo Updated</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'DELETE',
                            'method_name': 'delete_client_logo',
                            'name': 'Delete Client Logo',
                            'path': '/api/v1/client/{clientId}/logo'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request retrieves <strong>all '
                                           'findings</strong> for <strong>a specific '
                                           'client</strong>. The specific finding info returned is '
                                           'a truncated version of the full finding info. Sorting '
                                           'and filters can be added to the request body.</p>\n'
                                           '<p><strong>filters.by</strong></p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong><code>by</code></strong> '
                                           '<strong>Key</strong></th>\n'
                                           '<th><strong><code>value</code></strong> <strong>Data '
                                           'Type</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>searchTerm</td>\n'
                                           '<td>string</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>string</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>severity</td>\n'
                                           '<td>string</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>reportId</td>\n'
                                           '<td>integer</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>subStatus</td>\n'
                                           '<td>string</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>visibility</td>\n'
                                           '<td>string ("draft", or "published")</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>tags</td>\n'
                                           '<td>array of strings</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>commonIdentifiers</td>\n'
                                           '<td>array of strings representing CWE or CVE name i.e. '
                                           '["CWE-998", "CVE-2022-44268"]</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>dateFrom</td>\n'
                                           '<td>integer - milliseconds from epoch</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>dateTo</td>\n'
                                           '<td>integer - milliseconds from epoch</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>assignedTo</td>\n'
                                           '<td>string</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'list_client_findings',
                            'name': 'List Client Findings',
                            'path': '/api/v2/client/{clientId}/findings'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request retrieves <strong>assets associated '
                                           'with a specific client</strong>.</p>\n',
                            'folder_path': ['Clients'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'list_client_assets',
                            'name': 'List Client Assets',
                            'path': '/api/v2/clients/{clientId}/assets'}]},
 'content_library': {'display_name': 'Content Library',
                     'endpoints': [{'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request retrieves <strong>all '
                                                   'sections</strong> that exist in the '
                                                   '<strong>NarrativesDB</strong> module for a '
                                                   'tenant.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'list_all_sections',
                                    'name': 'List All Sections',
                                    'path': '/api/v2/narratives/sections/all'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request retrieves <strong>all '
                                                   'sections</strong> <strong>for a specific '
                                                   'repository</strong> exists in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'list_narrative_repository_sections',
                                    'name': 'List Narrative Repository Sections',
                                    'path': '/api/v2/narratives/{repositoryId}/sections'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request retrieves <strong>a specific '
                                                   'section</strong> that exist in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'get_narrative_repository_section',
                                    'name': 'Get Narrative Repository Section',
                                    'path': '/api/v2/narratives/sections/{sectionId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>creates a NarrativesDB '
                                                   'repository</strong> that is put in the '
                                                   '<strong>NarrativesDB</strong> module of the '
                                                   '<strong>Content Library</strong>.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'create_narratives_db_repository',
                                    'name': 'Create NarrativesDB Repository',
                                    'path': '/api/v2/narratives/createNarrativesRepository'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>creates a '
                                                   'section</strong> in the '
                                                   '<strong>NarrativesDB</strong> module of the '
                                                   '<strong>Content Library</strong>.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'create_narratives_repository_section',
                                    'name': 'Create Narratives Repository Section',
                                    'path': '/api/v2/narratives/sections'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>updates</strong> '
                                                   '<strong>a section</strong> that exists in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'PUT',
                                    'method_name': 'update_narrative_db_section',
                                    'name': 'Update NarrativeDB Section',
                                    'path': '/api/v2/narratives/sections/{sectionId}'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request deletes <strong>a section from '
                                                   'a specific repository</strong> in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'DELETE',
                                    'method_name': 'delete_narrative_db_section',
                                    'name': 'Delete NarrativeDB Section',
                                    'path': '/api/v2/narratives/{repositoryId}/sections/{sectionId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves a list of '
                                                   'all repositories</strong> that is in the '
                                                   '<strong>NarrativesDB</strong> module of the '
                                                   '<strong>Content Library</strong> based on the '
                                                   'user making the call and the permissionsLevel '
                                                   'body param.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'list_narrative_dbs',
                                    'name': 'List NarrativeDBs',
                                    'path': '/api/v2/narratives/getAllNarrativesRepositories'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>copies a '
                                                   'section</strong> <strong>to another '
                                                   'repository</strong> in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'NarrativesDB',
                                                    'Narratives (Sections)'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'copy_section_to_narative_repository',
                                    'name': 'Copy Section to Narative Repository',
                                    'path': '/api/v2/narratives/sections/copy'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves</strong> '
                                                   '<strong>all users</strong> that have been '
                                                   'added to repositories in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n'
                                                   '<p>Users can be added in the platform by '
                                                   'admins via the "Users &amp; Permissions" '
                                                   'option on the <strong>Repositories</strong> '
                                                   'tab of <strong>NarrativesDB</strong>.</p>\n',
                                    'folder_path': ['Content Library', 'NarrativesDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'get_all_narrative_db_users',
                                    'name': 'Get All NarrativeDB Users',
                                    'path': '/api/v2/narratives/users/all'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves '
                                                   'users</strong> for <strong>a specific '
                                                   'repository</strong> in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n'
                                                   '<p>Users can be added in the platform by '
                                                   'admins via the "Users &amp; Permissions" '
                                                   'option on the <strong>Repositories</strong> '
                                                   'tab of <strong>NarrativesDB</strong>.</p>\n',
                                    'folder_path': ['Content Library', 'NarrativesDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'get_narrative_db_users_by_repository',
                                    'name': 'Get NarrativeDB Users by Repository',
                                    'path': '/api/v2/narratives/{narrativeRepositoryId}/users'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>adds users</strong> to '
                                                   'a specific repository in the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n'
                                                   '<p>Only Standard users need to be added, as '
                                                   'Admins have access to all repositories.</p>\n'
                                                   '<p>When replace is set to '
                                                   '<strong>TRUE</strong> the repositoryUsers list '
                                                   'replaces the previous list. When set to '
                                                   '<strong>FALSE</strong>, it acts as an upsert '
                                                   'and will add new users or modify existing '
                                                   'users.</p>\n'
                                                   '<p>For example:</p>\n'
                                                   '<ul>\n'
                                                   '<li>Use replace is TRUE when one user exists '
                                                   'who no longer needs access and two different '
                                                   'users need to be added. If replace is set to '
                                                   'TRUE, the final list will only contain the two '
                                                   'new users and the first user will no longer '
                                                   'have access.</li>\n'
                                                   '<li>Use replace is FALSE when one user '
                                                   'currently has access and should continue '
                                                   'access, but two more users need access. If '
                                                   'replace is set to FALSE, the final list will '
                                                   'contain three users.</li>\n'
                                                   '</ul>\n'
                                                   '<p>Users can be added in the platform by '
                                                   'admins via the "Users &amp; Permissions" '
                                                   'option on the <strong>Repositories</strong> '
                                                   'tab of <strong>NarrativesDB</strong>.</p>\n',
                                    'folder_path': ['Content Library', 'NarrativesDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'PUT',
                                    'method_name': 'update_narrative_db_users_by_repository',
                                    'name': 'Update NarrativeDB Users by Repository',
                                    'path': '/api/v2/narratives/{narrativeRepositoryId}/users'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves a specific '
                                                   'repository</strong> and its metadata from the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'NarrativesDB'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'get_narrative_db',
                                    'name': 'Get NarrativeDB',
                                    'path': '/api/v2/narratives/{narrativeRepositoryId}/getNarrativesRepository'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>updates a specific '
                                                   'repository</strong> and its metadata from the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'NarrativesDB'],
                                    'graphql_query': None,
                                    'method': 'PUT',
                                    'method_name': 'update_narrative_db',
                                    'name': 'Update NarrativeDB',
                                    'path': '/api/v2/narratives/{narrativeRepositoryId}/updateNarrativesRepository'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request <strong>deletes a specific '
                                                   'repository</strong> from the '
                                                   '<strong>NarrativesDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'NarrativesDB'],
                                    'graphql_query': None,
                                    'method': 'DELETE',
                                    'method_name': 'delete_narrative_db',
                                    'name': 'Delete NarrativeDB',
                                    'path': '/api/v2/narratives/{narrativeRepositoryId}/deleteNarrativesRepository'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request retrieves <strong>all</strong> '
                                                   'WriteupsDB entries for a tenant.</p>\n'
                                                   '<p>The <code>instanceUrl</code> is needed to '
                                                   'execute the call.</p>\n'
                                                   '<p>Below is a list of the information that '
                                                   'will be returned on a successful call:</p>\n'
                                                   '<div class="click-to-expand-wrapper '
                                                   'is-table-wrapper"><table>\n'
                                                   '<thead>\n'
                                                   '<tr>\n'
                                                   '<th><strong>parameter</strong></th>\n'
                                                   '<th><strong>definition</strong></th>\n'
                                                   '<th><strong>example value</strong></th>\n'
                                                   '</tr>\n'
                                                   '</thead>\n'
                                                   '<tbody>\n'
                                                   '<tr>\n'
                                                   '<td>description</td>\n'
                                                   '<td>summary of writeup</td>\n'
                                                   '<td>The application responds to login '
                                                   "submissions with a link containing the user's "
                                                   'password within the URL query string.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>doc_id</td>\n'
                                                   '<td>document ID</td>\n'
                                                   '<td>104560</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>doc_type</td>\n'
                                                   '<td>document type</td>\n'
                                                   '<td>template</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>id</td>\n'
                                                   '<td>template ID</td>\n'
                                                   '<td>template_104560</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>recommendations</td>\n'
                                                   '<td>writeup recommendation</td>\n'
                                                   '<td>The application should never transmit any '
                                                   'sensitive information within the URL query '
                                                   'string. There is no good reason for a login '
                                                   'mechanism to echo passwords back to the user, '
                                                   'and the mechanism should be modified to remove '
                                                   'this behavior.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>references</td>\n'
                                                   '<td>writeup references</td>\n'
                                                   '<td>CWE-598: Information Exposure Through '
                                                   'Query Strings in GET Request</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>repositoryId</td>\n'
                                                   '<td>repository ID</td>\n'
                                                   '<td>cl0e3lc0c002318m</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>severity</td>\n'
                                                   '<td>writeup severity value</td>\n'
                                                   '<td></td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>source</td>\n'
                                                   '<td>writeup source</td>\n'
                                                   '<td>Burp</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>tenantId</td>\n'
                                                   '<td>tenant ID that writeup exists under</td>\n'
                                                   '<td>40632</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>title</td>\n'
                                                   '<td>writeup title</td>\n'
                                                   '<td>Password returned in URL query '
                                                   'string</td>\n'
                                                   '</tr>\n'
                                                   '</tbody>\n'
                                                   '</table>\n'
                                                   '</div>',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'list_writeups',
                                    'name': 'List Writeups',
                                    'path': '/api/v1/template/list'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request retrieves <strong>a '
                                                   'defined</strong> writeup.</p>\n'
                                                   '<p>The <code>instanceUrl</code> is needed to '
                                                   'execute the call.</p>\n'
                                                   '<p>Below is a list of the information that '
                                                   'will be returned on a successful call:</p>\n'
                                                   '<div class="click-to-expand-wrapper '
                                                   'is-table-wrapper"><table>\n'
                                                   '<thead>\n'
                                                   '<tr>\n'
                                                   '<th><strong>parameter</strong></th>\n'
                                                   '<th><strong>definition</strong></th>\n'
                                                   '<th><strong>example value</strong></th>\n'
                                                   '</tr>\n'
                                                   '</thead>\n'
                                                   '<tbody>\n'
                                                   '<tr>\n'
                                                   '<td>description</td>\n'
                                                   '<td>summary of writeup</td>\n'
                                                   '<td>The application responds to login '
                                                   "submissions with a link containing the user's "
                                                   'password within the URL query string.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>doc_id</td>\n'
                                                   '<td>document ID</td>\n'
                                                   '<td>104560</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>doc_type</td>\n'
                                                   '<td>document type</td>\n'
                                                   '<td>template</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>id</td>\n'
                                                   '<td>template ID</td>\n'
                                                   '<td>template_104560</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>recommendations</td>\n'
                                                   '<td>writeup recommendation</td>\n'
                                                   '<td>The application should never transmit any '
                                                   'sensitive information within the URL query '
                                                   'string. There is no good reason for a login '
                                                   'mechanism to echo passwords back to the user, '
                                                   'and the mechanism should be modified to remove '
                                                   'this behavior.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>references</td>\n'
                                                   '<td>writeup references</td>\n'
                                                   '<td>CWE-598: Information Exposure Through '
                                                   'Query Strings in GET Request</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>repositoryId</td>\n'
                                                   '<td>repository ID</td>\n'
                                                   '<td>cl0e3lc0c002318m</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>severity</td>\n'
                                                   '<td>writeup severity value</td>\n'
                                                   '<td></td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>source</td>\n'
                                                   '<td>writeup source</td>\n'
                                                   '<td>Burp</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>tenantId</td>\n'
                                                   '<td>tenant ID that writeup exists under</td>\n'
                                                   '<td>40632</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>title</td>\n'
                                                   '<td>writeup title</td>\n'
                                                   '<td>Password returned in URL query '
                                                   'string</td>\n'
                                                   '</tr>\n'
                                                   '</tbody>\n'
                                                   '</table>\n'
                                                   '</div>',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'get_writeup',
                                    'name': 'Get Writeup',
                                    'path': '/api/v1/template/{writeupId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>adds a new</strong> '
                                                   'writeup to a specific repository.</p>\n'
                                                   '<p>The <code>instanceUrl</code> is needed to '
                                                   'execute the call.</p>\n'
                                                   '<p>Below is a list of information needed to '
                                                   'fulfil the request.</p>\n'
                                                   '<div class="click-to-expand-wrapper '
                                                   'is-table-wrapper"><table>\n'
                                                   '<thead>\n'
                                                   '<tr>\n'
                                                   '<th><strong>parameter</strong></th>\n'
                                                   '<th><strong>definition</strong></th>\n'
                                                   '<th><strong>example value</strong></th>\n'
                                                   '</tr>\n'
                                                   '</thead>\n'
                                                   '<tbody>\n'
                                                   '<tr>\n'
                                                   '<td>title</td>\n'
                                                   '<td>title of writeup</td>\n'
                                                   '<td>The application responds to login '
                                                   "submissions with a link containing the user's "
                                                   'password within the URL query string.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>repositoryID</td>\n'
                                                   '<td>repository ID</td>\n'
                                                   '<td>cl0e3lc0c002318m</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>severity</td>\n'
                                                   '<td>severity of writeup (Critical, High, '
                                                   'Medium, Low and Informational)</td>\n'
                                                   '<td>Critical</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>description</td>\n'
                                                   '<td>description of writeup</td>\n'
                                                   '<td>The application responds to login '
                                                   "submissions with a link containing the user's "
                                                   'password within the URL query string.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>recommendations</td>\n'
                                                   '<td>writeup recommendation</td>\n'
                                                   '<td>The application should never transmit any '
                                                   'sensitive information within the URL query '
                                                   'string.</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>references</td>\n'
                                                   '<td>writeup references</td>\n'
                                                   '<td>CVE-2017-0267</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>fields</td>\n'
                                                   '<td>this is the parent parameter; each parent '
                                                   'requires an additional parameter label and '
                                                   'value</td>\n'
                                                   '<td>label: "Source"  <br />value: '
                                                   '"website"</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>tags</td>\n'
                                                   '<td>any tags associated with the writeup, to '
                                                   'be separated by a comma</td>\n'
                                                   '<td>pentest, enclave_99, crown_jewel</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>risk_score</td>\n'
                                                   '<td>used for CVSS 3.1 scores (other CVSS '
                                                   'version are handled in `fields`)</td>\n'
                                                   '<td></td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>calculated_severity</td>\n'
                                                   '<td>boolean of whether the finding severity '
                                                   'was set by the calculated CVSS3.1 score</td>\n'
                                                   '<td>true</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>common_identifiers</td>\n'
                                                   '<td>CVE and CWE data</td>\n'
                                                   '<td></td>\n'
                                                   '</tr>\n'
                                                   '</tbody>\n'
                                                   '</table>\n'
                                                   '</div><p><strong>Copy Finding to '
                                                   'WriteupsDB</strong></p>\n'
                                                   '<p>This endpoint should be used when creating '
                                                   'a new writeup based on a finding. Use the <a '
                                                   'href="https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc">GET '
                                                   'Get Finding</a> to get the finding, add the '
                                                   '<code>repositoryID</code> key, and send as the '
                                                   'payload of this request.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'create_writeups',
                                    'name': 'Create Writeups',
                                    'path': '/api/v1/template/create'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>updates</strong> an '
                                                   'existing writeup for a tenant.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'PUT',
                                    'method_name': 'update_writeups',
                                    'name': 'Update Writeups',
                                    'path': '/api/v1/template/{writeupId}'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request will <strong>delete</strong> a '
                                                   'writeup from <strong>WriteupsDB</strong> by '
                                                   'providing the instance url and writeup '
                                                   'ID.</p>\n'
                                                   '<p>The <code>instanceUrl</code> is needed to '
                                                   'execute the call.</p>\n'
                                                   '<p>When successful, the following parameters '
                                                   'will be returned:</p>\n'
                                                   '<div class="click-to-expand-wrapper '
                                                   'is-table-wrapper"><table>\n'
                                                   '<thead>\n'
                                                   '<tr>\n'
                                                   '<th><strong>parameter</strong></th>\n'
                                                   '<th><strong>definition</strong></th>\n'
                                                   '<th><strong>example value</strong></th>\n'
                                                   '</tr>\n'
                                                   '</thead>\n'
                                                   '<tbody>\n'
                                                   '<tr>\n'
                                                   '<td>message</td>\n'
                                                   '<td>validation of delete request</td>\n'
                                                   '<td>success</td>\n'
                                                   '</tr>\n'
                                                   '<tr>\n'
                                                   '<td>doc_id</td>\n'
                                                   '<td>ID of writeup deleted</td>\n'
                                                   '<td>template_104560</td>\n'
                                                   '</tr>\n'
                                                   '</tbody>\n'
                                                   '</table>\n'
                                                   '</div>',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'DELETE',
                                    'method_name': 'delete_writeups',
                                    'name': 'Delete Writeups',
                                    'path': '/api/v1/template/{writeupId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>Deprecated: See v2 endpoint <a '
                                                   'href="https://api-docs.plextrac.com/#83f5ce4b-572c-4de9-aa77-28c5943ce78a">Bulk '
                                                   'Add Writeups to Report</a> for similar '
                                                   'functionality.</p>\n'
                                                   '<p>This request will <strong>add a '
                                                   'writeup</strong> to a report.</p>\n'
                                                   '<p><strong>NOTE:</strong> The finding created '
                                                   "will have it's Date Reported set to the date "
                                                   'the Writeup was added to PT, not the date this '
                                                   'endpoint was called and the finding created in '
                                                   'the report.</p>\n'
                                                   '<p><strong>NOTE:</strong> Previous app '
                                                   'functionality was only to allow a writeup to '
                                                   'be added to a report once. We ahve since added '
                                                   'functionality to add a writeup to a report '
                                                   'multiple times and the created finding title '
                                                   'will have an incrementing numbered suffix. '
                                                   'This endpoint was not updated and you will '
                                                   'recieve a 409 Conflict error when attempting '
                                                   'to add a writeup multiple times. Use <a '
                                                   'href="https://api-docs.plextrac.com/#83f5ce4b-572c-4de9-aa77-28c5943ce78a">Bulk '
                                                   'Add Writeups to Report</a> instead.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'PUT',
                                    'method_name': 'add_writeup_to_report',
                                    'name': 'Add Writeup to Report',
                                    'path': '/api/v1/copy/{writeupId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request adds <strong>a '
                                                   'writeup</strong> in the '
                                                   '<strong>WriteupsDB</strong> module to an '
                                                   'existing report.</p>\n'
                                                   '<p>You will need the JSON object of the '
                                                   'writeup that you want to add to the report in '
                                                   'your request payload. To get this you need to '
                                                   'make another API request. You can use the <a '
                                                   'href="https://api-docs.plextrac.com/#865b782f-a5dd-43cf-bd6d-8bdabda1f5b2">List '
                                                   'Writeups</a> or <a '
                                                   'href="https://api-docs.plextrac.com/#cd707d09-1e7e-4bf0-9b97-92b48800821e">Get '
                                                   'Writeup</a> endpoints to get the writeup JSON '
                                                   'objects.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_add_writeups_to_report',
                                    'name': 'Bulk Add Writeups to Report',
                                    'path': '/api/v2/writeups/bulk/addToReport'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves all writeups '
                                                   'from a specific repository</strong> in the '
                                                   '<strong>WriteupsD</strong>B module.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'get_writeups_from_repository',
                                    'name': 'Get Writeups from Repository',
                                    'path': '/api/v2/repositories/{repositoryId}/getWriteups'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>moves a '
                                                   'writeup</strong> in the '
                                                   '<strong>WriteupsDB</strong> module to '
                                                   'different repository.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'add_writeups_to_repository',
                                    'name': 'Add Writeups to Repository',
                                    'path': '/api/v2/repositories/{repositoryId}/addWriteups'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p><strong>Deprecated</strong>: Since this '
                                                   "endpoint's payload requires the finding "
                                                   'object, it proves the same functionality as <a '
                                                   'href="https://api-docs.plextrac.com/#ebbc5cf9-f24c-41ea-a393-558f1f3e0529">POST '
                                                   'Create Writeups</a> which should be used '
                                                   'instead.</p>\n'
                                                   '<p>This request <strong>copies a finding from '
                                                   'a report</strong> and puts into a '
                                                   '<strong>WriteUpsDB</strong> repository.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'copy_finding_to_writeups_repository',
                                    'name': 'Copy Finding to Writeups Repository',
                                    'path': '/api/v2/repositories/copyFlawToWriteupsRepository'},
                                   {'aliases': [],
                                    'body_mode': 'formdata',
                                    'default_params': [],
                                    'description': '<p>This request <strong>imports a csv of '
                                                   'writeups</strong> to the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n'
                                                   '<p>In the URL the source should be '
                                                   '<code>csv</code>.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'import_writeups_to_repository',
                                    'name': 'Import Writeups to Repository',
                                    'path': '/api/v2/writeups/import/{source}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request removes <strong>a writeup from '
                                                   'a specific repository</strong> in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'remove_writeups_from_repository',
                                    'name': 'Remove Writeups from Repository',
                                    'path': '/api/v2/repositories/{repositoryId}/removeWriteup'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>copies writeups from a '
                                                   'repository</strong> in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_copy_writeups',
                                    'name': 'Bulk Copy Writeups',
                                    'path': '/api/v2/writeups/bulk/copy'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>moves a writeup to '
                                                   'another repository</strong> in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_move_writeups',
                                    'name': 'Bulk Move Writeups',
                                    'path': '/api/v2/writeups/bulk/move'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>adds tags to a '
                                                   'writeup</strong> in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_add_tags_to_writeups',
                                    'name': 'Bulk Add Tags to Writeups',
                                    'path': '/api/v2/writeups/bulk/tags'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>bulk deletes a list of '
                                                   'writeups</strong>, removing them from any '
                                                   'repositories, in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n'
                                                   '<p>You must use the <code>doc_id</code> of any '
                                                   'writeups in the list of writeups in the '
                                                   'payload.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Writeups'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'bulk_delete_writeups',
                                    'name': 'Bulk Delete Writeups',
                                    'path': '/api/v2/writeups/bulk/delete'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves a list of '
                                                   'repositories</strong> in the '
                                                   '<strong>WriteupsD</strong>B module.</p>\n'
                                                   '<p>Must send an empty JSON object with the '
                                                   'request.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'WriteupsDB',
                                                    'Repositories'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'list_all_writeup_repositories',
                                    'name': 'List All Writeup Repositories',
                                    'path': '/api/v2/repositories/getAllWriteupsRepositories'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>If the user has the RBAC permission '
                                                   '<code>ACCESS_WRITEUPS_REPOSITORIES</code>, '
                                                   'this request <strong>retrieves a list of '
                                                   'repositories</strong> in the '
                                                   '<strong>WriteupsD</strong>B module that the '
                                                   'user is assigned an EDITOR on.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'WriteupsDB',
                                                    'Repositories'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'get_writeups_repository_users_can_edit',
                                    'name': 'Get Writeups Repository Users Can Edit',
                                    'path': '/api/v2/repositories/listUserCanEdit'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves a specific '
                                                   'repository and associated metadata</strong> in '
                                                   'the <strong>WriteupsDB</strong> module.</p>\n'
                                                   '<p>The <code>repositoryID</code> is found in '
                                                   'the url when viewing the repository:</p>\n'
                                                   '<ol>\n'
                                                   '<li>Open PlexTrac.</li>\n'
                                                   '<li>Expand "Content Library" pulldown in the '
                                                   'main menu.</li>\n'
                                                   '<li>Click <strong>WriteupsDB</strong>.</li>\n'
                                                   '<li>Click the desired repository.</li>\n'
                                                   '<li>Inspect the url. It is the value between '
                                                   '"repository" and "writeups."</li>\n'
                                                   '</ol>\n'
                                                   '<p>.../repository/<strong>cl0e3lc0c002318mx4y2bg3wn</strong>/writeups</p>\n',
                                    'folder_path': ['Content Library',
                                                    'WriteupsDB',
                                                    'Repositories'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'get_writeup_repository',
                                    'name': 'Get Writeup Repository',
                                    'path': '/api/v2/repositories/{repositoryId}'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>adds a new '
                                                   'repository</strong> in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'WriteupsDB',
                                                    'Repositories'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'create_writeup_repository',
                                    'name': 'Create Writeup Repository',
                                    'path': '/api/v2/repositories/add'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>updates a specific '
                                                   'repository and associated metadata</strong> in '
                                                   'the <strong>WriteupsDB</strong> module.</p>\n'
                                                   '<p>The <code>repositoryID</code> is found in '
                                                   'the url when viewing the repository:</p>\n'
                                                   '<ol>\n'
                                                   '<li>Open PlexTrac.</li>\n'
                                                   '<li>Expand "Content Library" pulldown in the '
                                                   'main menu.</li>\n'
                                                   '<li>Click <strong>WriteupsDB</strong>.</li>\n'
                                                   '<li>Click the desired repository.</li>\n'
                                                   '<li>Inspect the url. It is the value between '
                                                   '"repository" and "writeups."</li>\n'
                                                   '</ol>\n'
                                                   '<p>.../repository/<strong>cl0e3lc0c002318mx4y2bg3wn</strong>/writeups</p>\n',
                                    'folder_path': ['Content Library',
                                                    'WriteupsDB',
                                                    'Repositories'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'update_writeup_repository',
                                    'name': 'Update Writeup Repository',
                                    'path': '/api/v2/repositories/{repositoryId}/update'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>deletes a '
                                                   'repository</strong> in the '
                                                   '<strong>WriteupsDB</strong> module.</p>\n',
                                    'folder_path': ['Content Library',
                                                    'WriteupsDB',
                                                    'Repositories'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'delete_writeup_repository',
                                    'name': 'Delete Writeup Repository',
                                    'path': '/api/v2/repositories/delete'},
                                   {'aliases': [],
                                    'body_mode': 'none',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves all users '
                                                   'from a specific repository</strong> in the '
                                                   '<strong>WriteupsD</strong>B module.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'GET',
                                    'method_name': 'get_writeups_repository_users',
                                    'name': 'Get Writeups Repository Users',
                                    'path': '/api/v2/repositories/{repositoryId}/users'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>adds users to a '
                                                   'specific repository</strong> in the '
                                                   '<strong>WriteupsD</strong>B module by adding a '
                                                   'new user entry for each user in the list sent '
                                                   'to the endpoint.</p>\n'
                                                   '<p>The userId will be used to lookup a user in '
                                                   "the Plextrac instance. That user's name and "
                                                   'email will be used instead of the data passed '
                                                   'into this payload.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'add_writeups_repository_users',
                                    'name': 'Add Writeups Repository Users',
                                    'path': '/api/v2/repositories/{repositoryId}/users'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>replaces the current '
                                                   'list of users with a new one for a specific '
                                                   'repository</strong> in the '
                                                   '<strong>WriteupsD</strong>B module.</p>\n'
                                                   '<p>Any users not on the list provided will be '
                                                   'removed and no longer have access.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'PUT',
                                    'method_name': 'update_writeups_repository_users',
                                    'name': 'Update Writeups Repository Users',
                                    'path': '/api/v2/repositories/{repositoryId}/users'},
                                   {'aliases': [],
                                    'body_mode': 'raw',
                                    'default_params': [],
                                    'description': '<p>This request <strong>retrieves a list of '
                                                   'users</strong> in the '
                                                   '<strong>WriteupsD</strong>B module with the '
                                                   '<code>MANAGE_WRITEUPS_REPOSITORIES</code> RBAC '
                                                   'permission and returns the list filter by and '
                                                   'user that has the <code>filterText</code> in '
                                                   'the <code>first name</code>, <code>last '
                                                   'name</code>, or <code>email</code> '
                                                   'field.</p>\n',
                                    'folder_path': ['Content Library', 'WriteupsDB', 'Users'],
                                    'graphql_query': None,
                                    'method': 'POST',
                                    'method_name': 'get_all_writeups_repository_users',
                                    'name': 'Get All Writeups Repository Users',
                                    'path': '/api/v2/repositories/users'}]},
 'files': {'display_name': 'Files',
           'endpoints': [{'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Return a list of filtered artifact files.</p>\n'
                                         '<p>The <code>components</code> property is '
                                         'optional.</p>\n',
                          'folder_path': ['Files', 'Artifacts'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'get_artifacts',
                          'name': 'Get artifacts',
                          'path': '/api/v1/file-manager/artifacts'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '',
                          'folder_path': ['Files', 'Artifacts'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'download_an_artifact',
                          'name': 'Download an artifact',
                          'path': '/api/v1/file-manager/artifacts/{artifactId}'},
                         {'aliases': [],
                          'body_mode': 'formdata',
                          'default_params': [],
                          'description': '<p>Uploads a file to the tenant. These files live in a '
                                         'single location and are related to clients and reports '
                                         'through the <code>relations</code> attribute. Each file '
                                         'has a list of <code>components</code> or categorys it '
                                         'belongs to. This is used for filtering when loading '
                                         'files to display in platform. Files with different '
                                         'components are displayed in different locations.</p>\n'
                                         '<p><strong>Components used in platform:</strong></p>\n'
                                         '<p>report_artifacts</p>\n'
                                         '<p><strong>Relation models used in '
                                         'platform:</strong></p>\n'
                                         '<p>{"model":"client","id":"1234"}</p>\n'
                                         '<p>{"model":"report","id":"123456"}</p>\n'
                                         '<p>{"model":"assessment_question","id":"clc0syuip005a0zo3cv3p87ic"}</p>\n'
                                         '<p><strong>Accepted file MIME types:</strong></p>\n'
                                         "<p>'application/x-python-code',<br "
                                         "/>'applicaiton/x-python',<br />'application/json',<br "
                                         "/>'application/pdf',<br />'application/xml',<br "
                                         "/>'application/msword',<br "
                                         "/>'application/octet-stream',<br "
                                         "/>'application/vnd.openxmlformats-officedocument.wordprocessingml.document',<br "
                                         "/>'application/vnd.ms-excel',<br "
                                         "/>'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',<br "
                                         "/>'application/vnd.oasis.opendocument.text',<br "
                                         "/>'application/x-zip-compressed',<br "
                                         "/>'application/vnd.oasis.opendocument.spreadsheet',<br "
                                         "/>'application/zip',<br "
                                         "/>'application/x-7z-compressed',<br />'image/bmp',<br "
                                         "/>'image/gif',<br />'image/jpeg',<br />'image/png',<br "
                                         "/>'text/plain',<br />'text/html',<br />'text/xml',<br "
                                         "/>'text/x-python',<br />'text/x-python-script',<br "
                                         "/>'text/x-sh',<br />'text/javascript',<br "
                                         "/>'text/csv',<br />'video/mp4',<br "
                                         "/>'video/quicktime',<br />'video/mpeg',<br "
                                         "/>'video/x-msvideo',<br />'video/x-ms-wmv'</p>\n",
                          'folder_path': ['Files', 'Artifacts'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'upload_an_artifact_file',
                          'name': 'Upload an artifact (file)',
                          'path': '/api/v1/file-manager/upload'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request <strong>deletes an artifact</strong> '
                                         'from the tenant.</p>\n'
                                         '<p>Will return a 404 error if an artifact is not found '
                                         'with the provided <code>artifactId</code>.</p>\n',
                          'folder_path': ['Files', 'Artifacts'],
                          'graphql_query': None,
                          'method': 'DELETE',
                          'method_name': 'delete_an_artifact',
                          'name': 'Delete an artifact',
                          'path': '/api/v1/file-manager/artifacts/{artifactId}'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This endpoint returns an inline image that was pasted '
                                         'in a rich text CKE field in the platform.</p>\n'
                                         '<p><strong>Authentication:</strong></p>\n'
                                         '<p>This endpoint has a non standard authentication '
                                         'workflow that is based solely on cookies. When '
                                         'authenticating to Plextrac with the normal '
                                         'authentication endpoint, there is a <code>cookie</code> '
                                         'and <code>token</code> value returned in the response. '
                                         "For the <strong>Get Upload by Name</strong> endpoint's "
                                         'authentication you need to send the <code>cookie</code> '
                                         'value as a cookie in the request. The <code>token</code> '
                                         'value, normally sent as the JWT Authorization header, '
                                         'should not be sent or you will get a 401 error.</p>\n'
                                         '<p>Cookies consists of a name, value, and additional '
                                         'attributes. The cookie used for authentication on this '
                                         'endpoint has the follwoing:</p>\n'
                                         '<p><strong>name</strong>: "token"</p>\n'
                                         '<p><strong>value</strong>: <code>cookie</code> value '
                                         'from authentication endpoint response</p>\n',
                          'folder_path': ['Files'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_upload_by_name',
                          'name': 'Get Upload by Name',
                          'path': '/api/v1/uploads/9bee9f28-7e25-4b4f-8b64-b520fc3c0b7c.png'},
                         {'aliases': [],
                          'body_mode': 'formdata',
                          'default_params': [],
                          'description': '',
                          'folder_path': ['Files'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'upload_image_to_tenant',
                          'name': 'Upload Image to Tenant',
                          'path': '/api/v1/uploads'}]},
 'findings': {'display_name': 'Findings',
              'endpoints': [{'aliases': [],
                             'body_mode': 'formdata',
                             'default_params': [],
                             'description': '<p><strong>DEPRECATED</strong>: Please use <a '
                                            'href="https://api-docs.plextrac.com/#e0eff080-a18b-4049-9df3-7218a13465a7">Findings '
                                            'from Tools - Streaming Upload</a></p>\n'
                                            '<p><code>source</code> must be from the following '
                                            'list:</p>\n'
                                            '<p>burp<br />burphtml<br />horizon<br />nessus<br '
                                            '/>nexpose<br />ptrac<br />veracode</p>\n',
                             'folder_path': ['Findings', 'Findings From Tools V2'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'add_findings_from_file_imports',
                             'name': 'Add Findings from File Imports V2',
                             'path': '/api/v2/client/{clientId}/report/{reportId}/importAsync/{source}'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Findings', 'Findings from Tools - Streaming Upload'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'request_presigned_url',
                             'name': 'Request Presigned URL',
                             'path': '/api/v2/presigned-url '},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Findings', 'Findings from Tools - Streaming Upload'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'add_findings_async_from_preuploaded_file_imports',
                             'name': 'Add Findings Async from Preuploaded File Imports',
                             'path': '/api/v2/client/{clientId}/report/{reportId}/preuploaded-import/{source}'},
                            {'aliases': [],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '<p>Import Status events have a lifetime of 1 hr. Once '
                                            'expired there are removed and will no longer be '
                                            "returned on this endpoint's response.</p>\n",
                             'folder_path': ['Findings', 'Findings from Tools - Streaming Upload'],
                             'graphql_query': None,
                             'method': 'GET',
                             'method_name': 'get_import_status',
                             'name': 'Get Import Status',
                             'path': '/api/v2/my-imports'},
                            {'aliases': [],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Findings', 'Evidence'],
                             'graphql_query': None,
                             'method': 'GET',
                             'method_name': 'get_scanner_output',
                             'name': 'Get Scanner Output',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>Deprecated: Please use <strong>GET Get Scanner '
                                            'Output</strong></p>\n'
                                            '<p>This request <strong>retrieves evidence '
                                            'information</strong> for a specific finding for a '
                                            'specific report.</p>\n',
                             'folder_path': ['Findings', 'Evidence'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'bulk_get_evidence',
                             'name': 'Bulk Get Evidence',
                             'path': '/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This request <strong>updates evidence for a '
                                            'specific asset and finding</strong>.</p>\n',
                             'folder_path': ['Findings', 'Evidence'],
                             'graphql_query': None,
                             'method': 'PUT',
                             'method_name': 'update_evidence',
                             'name': 'Update Evidence',
                             'path': '/api/v2/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This request <strong>inserts evidence information '
                                            'in bulk</strong> to an affected asset on a finding. '
                                            'This can either update existing evidence or create '
                                            'new evidence.</p>\n'
                                            '<p><strong>Note:</strong> The <code>id</code> should '
                                            'be an existing or new UUID.</p>\n'
                                            '<p><strong>Note:</strong> The <code>assets</code> '
                                            'property should be an array with a single asset ID. '
                                            'The evidence on an affected asset is built by quering '
                                            "which evidence is related to a finding's affected "
                                            'asset. Creating a new piece of evidence with the '
                                            'finding ID and asset ID will effectively link the '
                                            'evidence to the affected asset.</p>\n',
                             'folder_path': ['Findings', 'Evidence'],
                             'graphql_query': None,
                             'method': 'PUT',
                             'method_name': 'bulk_upsert_evidence',
                             'name': 'Bulk Upsert Evidence',
                             'path': '/api/v2/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence'},
                            {'aliases': [],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '<p>This request <strong>retrieves a list of findings '
                                            'for a specific report</strong>.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'GET',
                             'method_name': 'list_report_findings',
                             'name': 'List Report Findings',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaws'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p><strong>Breaking Change '
                                            'Notification:</strong></p>\n'
                                            '<p>The 99999 pagination limit option will be remove '
                                            'in 2.23.</p>\n'
                                            '<p>.</p>\n'
                                            '<p>This request <strong>retrieves a list of findings '
                                            'for a specific report.</strong></p>\n'
                                            '<p><code>pagination</code> is a required key while '
                                            '<code>sort</code> and <code>filters</code> are '
                                            'optional.</p>\n'
                                            '<p>The <code>pagination.limit</code> must be one of '
                                            '[1, 10, 50, 100, 99999]. The '
                                            '<code>pagination.offset</code> is the number of '
                                            'records to shift by, not the number of pages to shift '
                                            'by. i.e. offset 2, limit 10 gives you records 2-12 '
                                            'not 20-30</p>\n'
                                            '<p>The following values can be used in the '
                                            '<code>filters.by</code> field:</p>\n'
                                            '<ul>\n'
                                            '<li><p>findingTags</p>\n'
                                            '</li>\n'
                                            '<li><p>searchTerm</p>\n'
                                            '</li>\n'
                                            '<li><p>createdAt</p>\n'
                                            '</li>\n'
                                            '<li><p>updatedAt</p>\n'
                                            '</li>\n'
                                            '<li><p>reopenedAt</p>\n'
                                            '</li>\n'
                                            '<li><p>closedAt</p>\n'
                                            '</li>\n'
                                            '<li><p>assignedTo</p>\n'
                                            '</li>\n'
                                            '<li><p>flaw_id</p>\n'
                                            '</li>\n'
                                            '<li><p>client_id</p>\n'
                                            '</li>\n'
                                            '<li><p>report_id</p>\n'
                                            '</li>\n'
                                            '<li><p>severity</p>\n'
                                            '</li>\n'
                                            '<li><p>source</p>\n'
                                            '</li>\n'
                                            '<li><p>status</p>\n'
                                            '</li>\n'
                                            '<li><p>subStatus</p>\n'
                                            '</li>\n'
                                            '<li><p>title</p>\n'
                                            '</li>\n'
                                            '<li><p>visibility</p>\n'
                                            '</li>\n'
                                            '</ul>\n'
                                            '<p>The following values can be used in the '
                                            '<code>sort.by</code> field:</p>\n'
                                            '<ul>\n'
                                            '<li><p>assignedTo</p>\n'
                                            '</li>\n'
                                            '<li><p>clientId</p>\n'
                                            '</li>\n'
                                            '<li><p>createdAt</p>\n'
                                            '</li>\n'
                                            '<li><p>updatedAt</p>\n'
                                            '</li>\n'
                                            '<li><p>reopenedAt</p>\n'
                                            '</li>\n'
                                            '<li><p>closedAt</p>\n'
                                            '</li>\n'
                                            '<li><p>flawId</p>\n'
                                            '</li>\n'
                                            '<li><p>reportId</p>\n'
                                            '</li>\n'
                                            '<li><p>severity</p>\n'
                                            '</li>\n'
                                            '<li><p>source</p>\n'
                                            '</li>\n'
                                            '<li><p>status</p>\n'
                                            '</li>\n'
                                            '<li><p>subStatus</p>\n'
                                            '</li>\n'
                                            '<li><p>title</p>\n'
                                            '</li>\n'
                                            '<li><p>visibility</p>\n'
                                            '</li>\n'
                                            '<li><p>cvss3_1</p>\n'
                                            '</li>\n'
                                            '<li><p>cve_id</p>\n'
                                            '</li>\n'
                                            '<li><p>cwe_id</p>\n'
                                            '</li>\n'
                                            '</ul>\n'
                                            '<p>The following values can be used in the '
                                            '<code>sort.order</code> field:</p>\n'
                                            '<ul>\n'
                                            '<li><p>ASC</p>\n'
                                            '</li>\n'
                                            '<li><p>DESC</p>\n'
                                            '</li>\n'
                                            '</ul>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'get_findings_by_report',
                             'name': 'Get Findings by Report',
                             'path': '/api/v2/clients/{clientId}/reports/{reportId}/findings'},
                            {'aliases': ['get'],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '<p>This request <strong>retrieves a specific '
                                            'finding</strong> from a report.</p>\n'
                                            '<p>See our docs on the <a '
                                            'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/finding-object">Finding '
                                            'Object</a> structure for more details on the '
                                            'response.</p>\n'
                                            '<p><strong>Required RBAC Permissions:</strong></p>\n'
                                            '<ul>\n'
                                            '<li><p><code>View Reports</code></p>\n'
                                            '</li>\n'
                                            '<li><p><code>View Report Findings</code></p>\n'
                                            '</li>\n'
                                            '</ul>\n'
                                            '<p>This only returns <strong>Published</strong> '
                                            'findings, unless the user also has the <code>Ability '
                                            'to mark a finding as published</code> '
                                            'permission.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'GET',
                             'method_name': 'get_finding',
                             'name': 'Get Finding',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}'},
                            {'aliases': ['create'],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This request <strong>creates a finding</strong> '
                                            'for a specific report.</p>\n'
                                            '<p>See our docs on the <a '
                                            'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/finding-object">Finding '
                                            'Object</a> structure for more details on possible '
                                            'keys.</p>\n'
                                            '<p><strong>Affected Assets</strong></p>\n'
                                            "<p>A finding's <code>affected_assets</code> are a "
                                            'copy of a <code>client_asset</code> with additional '
                                            'affected fields. An asset should already be created '
                                            'on the client before adding to a finding. Get the ID '
                                            'and name of the client asset, then create an entry '
                                            "for the finding's <code>affected_assets</code> with "
                                            'all of the following keys. See the example below for '
                                            'the payload JSON structure. See our docs on the <a '
                                            'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object">Asset '
                                            'Object</a> structure for more details about these '
                                            'affected fields.</p>\n'
                                            '<ul>\n'
                                            '<li><p>id</p>\n'
                                            '</li>\n'
                                            '<li><p>asset (name of asset)</p>\n'
                                            '</li>\n'
                                            '<li><p>ports</p>\n'
                                            '</li>\n'
                                            '<li><p>status</p>\n'
                                            '</li>\n'
                                            '<li><p>locationUrl</p>\n'
                                            '</li>\n'
                                            '<li><p>vulnerableParameters</p>\n'
                                            '</li>\n'
                                            '<li><p>evidence</p>\n'
                                            '</li>\n'
                                            '<li><p>notes</p>\n'
                                            '</li>\n'
                                            '</ul>\n'
                                            '<p>Then add this created asset object to the '
                                            "finding's <code>affected_assets</code> dictionary "
                                            "with the key being a string of the asset's "
                                            '<code>id</code> and the value being the JSON asset '
                                            'object.</p>\n'
                                            '<p><strong>Registering Tags</strong></p>\n'
                                            '<p>When a finding is created in the UI there are a '
                                            'few processes that get kicked off that do not happen '
                                            'when calling this endpoint directly.</p>\n'
                                            '<p>Any tags added to the finding that have not been '
                                            'added anywhere else in the instance will be added to '
                                            'the finding but NOT to the list of tenant tags. This '
                                            'means when you start typing to add a tag anywhere in '
                                            'the platform, the dropdown list that pops up will not '
                                            "have the new tags since they weren't added to the "
                                            'listed of tenant tags.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'create_finding',
                             'name': 'Create Finding',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/create'},
                            {'aliases': ['update'],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This request <strong>updates a specific '
                                            'finding</strong> for a specific report.</p>\n'
                                            '<p>See our docs on the <a '
                                            'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/finding-object">Finding '
                                            'Object</a> structure for more details on possible '
                                            'keys.</p>\n'
                                            '<p><strong>Note:</strong></p>\n'
                                            '<p>This PUT request is meant to '
                                            '<strong>replace</strong> the finding object in the DB '
                                            "and doesn't contain all system validation checks, "
                                            'however the payload is still selectively parsed like '
                                            'a quasi PATCH endpoint. Use the <a '
                                            'href="https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc">GET '
                                            'Get Finding</a> endpoint to get the current finding, '
                                            'pull the proprties that need to be changed, then send '
                                            'that object in the payload to update the '
                                            'finding.</p>\n'
                                            '<p>The example payloads shown here do not have all '
                                            'the possible properties on a finding, but only acts '
                                            'as an example. Each finding will be slightly '
                                            'different depending on what data is on the finding. '
                                            "Some property keys won't be added to a finding until "
                                            'that data is added to the finding.</p>\n'
                                            '<p><strong>Affected Assets</strong></p>\n'
                                            "<p>A finding's <code>affected_assets</code> are a "
                                            'copy of a <code>client_asset</code> with additional '
                                            'affected fields. When <strong>adding a new</strong> '
                                            "asset to a finding's affected_assets, you should use "
                                            'the GET Get Asset endpoint, then add the following '
                                            'keys:</p>\n'
                                            '<ul>\n'
                                            '<li><p>ports</p>\n'
                                            '</li>\n'
                                            '<li><p>status</p>\n'
                                            '</li>\n'
                                            '<li><p>locationUrl</p>\n'
                                            '</li>\n'
                                            '<li><p>vulnerableParameters</p>\n'
                                            '</li>\n'
                                            '<li><p>evidence</p>\n'
                                            '</li>\n'
                                            '<li><p>notes</p>\n'
                                            '</li>\n'
                                            '</ul>\n'
                                            '<p>Then add this modified asset object to the '
                                            "finding's <code>affected_assets</code> dictionary "
                                            "with the key being a string of the asset's "
                                            '<code>id</code> and the value being the modified '
                                            'asset object.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'PUT',
                             'method_name': 'update_finding',
                             'name': 'Update Finding',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>Bulk actions for updating findings. You can '
                                            '<strong>add tags</strong>, change the <strong>created '
                                            'at data</strong> or set the <strong>draft/published '
                                            'status</strong> with tthis endpoint.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'PUT',
                             'method_name': 'bulk_update_findings',
                             'name': 'Bulk Update Findings',
                             'path': '/api/v2/clients/{clientId}/reports/{reportId}/findings'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>Bulk actions for updating findings. You can update '
                                            'the status, sub-status, and assinged user with this '
                                            'endpoint.</p>\n'
                                            '<p>Note: If</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'PUT',
                             'method_name': 'bulk_update_findings_assign_update_status',
                             'name': 'Bulk Update Findings - Assign / Update Status',
                             'path': '/api/v2/client/{clientId}/findings'},
                            {'aliases': ['delete'],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '<p>This request <strong>deletes a specific '
                                            'finding</strong> from a specific report.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'DELETE',
                             'method_name': 'delete_finding',
                             'name': 'Delete Finding',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This request <strong>enables a bulk deletion of '
                                            'findings</strong> from a report.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'bulk_delete_findings',
                             'name': 'Bulk Delete Findings',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaws/delete'},
                            {'aliases': [],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '<p>This request <strong>retrieves the status of a '
                                            'specific finding</strong> from a report.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'GET',
                             'method_name': 'get_finding_status_list',
                             'name': 'Get Finding Status List',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This request <strong>updates the status of a '
                                            'specific finding</strong> from a report.</p>\n',
                             'folder_path': ['Findings'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'create_status_update',
                             'name': 'Create Status Update',
                             'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/status/update'}]},
 'graph_ql_mutations': {'display_name': 'Graph QL Mutations',
                        'endpoints': [{'aliases': [],
                                       'body_mode': 'graphql',
                                       'default_params': [],
                                       'description': '<p>Update individual properties on a '
                                                      'finding.</p>\n'
                                                      '<p>StartFragment</p>\n'
                                                      '<p><strong>NOTE:</strong> The Custom Fields '
                                                      'tab of a finding in the platform is '
                                                      'considered a single property.</p>\n'
                                                      '<pre class="click-to-expand-wrapper '
                                                      'is-snippet-wrapper"><code '
                                                      'class="language-json">"data": {\n'
                                                      '    "fields": [\n'
                                                      '        {\n'
                                                      '            "key": "synopsis",\n'
                                                      '            "label": "Synopsis",\n'
                                                      '            "value": "The remote OS or '
                                                      'service pack is no longer supported. test"\n'
                                                      '        },\n'
                                                      '        {\n'
                                                      '            "key": "evidence",\n'
                                                      '            "label": "Evidence",\n'
                                                      '            "value": ""\n'
                                                      '        }\n'
                                                      '    ]\n'
                                                      '}\n'
                                                      '\n'
                                                      '</code></pre>\n'
                                                      '<p>This means to update to any custom field '
                                                      'key, label, or value you will need to send '
                                                      'the entire <code>fields</code> object in '
                                                      'the <code>data</code> property.</p>\n'
                                                      '<p>EndFr</p>\n',
                                       'folder_path': ['Graph QL Mutations'],
                                       'graphql_query': 'mutation FindingUpdate($clientId: Int!, '
                                                        '$data: FindingUpdateInput!, $findingId: '
                                                        'Float!, $reportId: Int!) {\r\n'
                                                        '  findingUpdate(\r\n'
                                                        '    clientId: $clientId\r\n'
                                                        '    data: $data\r\n'
                                                        '    findingId: $findingId\r\n'
                                                        '    reportId: $reportId\r\n'
                                                        '  ) {\r\n'
                                                        '    ... on FindingUpdateSuccess {\r\n'
                                                        '      finding {\r\n'
                                                        '        ...FindingFragment\r\n'
                                                        '        __typename\r\n'
                                                        '      }\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '}\r\n'
                                                        '\r\n'
                                                        'fragment FindingFragment on Finding {\r\n'
                                                        '  assignedTo\r\n'
                                                        '  closedAt\r\n'
                                                        '  createdAt\r\n'
                                                        '  code_samples {\r\n'
                                                        '    caption\r\n'
                                                        '    code\r\n'
                                                        '    id\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  common_identifiers {\r\n'
                                                        '    CVE {\r\n'
                                                        '      name\r\n'
                                                        '      id\r\n'
                                                        '      year\r\n'
                                                        '      link\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    CWE {\r\n'
                                                        '      name\r\n'
                                                        '      id\r\n'
                                                        '      link\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  description\r\n'
                                                        '  exhibits {\r\n'
                                                        '    assets {\r\n'
                                                        '      asset\r\n'
                                                        '      id\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    caption\r\n'
                                                        '    exhibitID\r\n'
                                                        '    index\r\n'
                                                        '    type\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  fields {\r\n'
                                                        '    key\r\n'
                                                        '    label\r\n'
                                                        '    value\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  flaw_id\r\n'
                                                        '  includeEvidence\r\n'
                                                        '  recommendations\r\n'
                                                        '  references\r\n'
                                                        '  scores\r\n'
                                                        '  selectedScore\r\n'
                                                        '  severity\r\n'
                                                        '  source\r\n'
                                                        '  status\r\n'
                                                        '  subStatus\r\n'
                                                        '  tags\r\n'
                                                        '  title\r\n'
                                                        '  visibility\r\n'
                                                        '  calculated_severity\r\n'
                                                        '  risk_score {\r\n'
                                                        '    CVSS3_1 {\r\n'
                                                        '      overall\r\n'
                                                        '      vector\r\n'
                                                        '      subScore {\r\n'
                                                        '        base\r\n'
                                                        '        temporal\r\n'
                                                        '        environmental\r\n'
                                                        '        __typename\r\n'
                                                        '      }\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    CVSS3 {\r\n'
                                                        '      overall\r\n'
                                                        '      vector\r\n'
                                                        '      subScore {\r\n'
                                                        '        base\r\n'
                                                        '        temporal\r\n'
                                                        '        environmental\r\n'
                                                        '        __typename\r\n'
                                                        '      }\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    CVSS2 {\r\n'
                                                        '      overall\r\n'
                                                        '      vector\r\n'
                                                        '      subScore {\r\n'
                                                        '        base\r\n'
                                                        '        temporal\r\n'
                                                        '        __typename\r\n'
                                                        '      }\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    CWSS {\r\n'
                                                        '      overall\r\n'
                                                        '      vector\r\n'
                                                        '      subScore {\r\n'
                                                        '        base\r\n'
                                                        '        environmental\r\n'
                                                        '        attackSurface\r\n'
                                                        '        __typename\r\n'
                                                        '      }\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  hackerOneData {\r\n'
                                                        '    bountyAmount\r\n'
                                                        '    programId\r\n'
                                                        '    programName\r\n'
                                                        '    remoteId\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  snykData {\r\n'
                                                        '    issueType\r\n'
                                                        '    pkgName\r\n'
                                                        '    issueUrl\r\n'
                                                        '    identifiers {\r\n'
                                                        '      CVE\r\n'
                                                        '      CWE\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    exploitMaturity\r\n'
                                                        '    patches\r\n'
                                                        '    nearestFixedInVersion\r\n'
                                                        '    isMaliciousPackage\r\n'
                                                        '    violatedPolicyPublicId\r\n'
                                                        '    introducedThrough\r\n'
                                                        '    fixInfo {\r\n'
                                                        '      isUpgradable\r\n'
                                                        '      isPinnable\r\n'
                                                        '      isPatchable\r\n'
                                                        '      isFixable\r\n'
                                                        '      isPartiallyFixable\r\n'
                                                        '      nearestFixedInVersion\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  edgescanData {\r\n'
                                                        '    id\r\n'
                                                        '    portal_url\r\n'
                                                        '    details {\r\n'
                                                        '      html\r\n'
                                                        '      id\r\n'
                                                        '      orginal_detail_hash\r\n'
                                                        '      parameter_name\r\n'
                                                        '      parameter_type\r\n'
                                                        '      port\r\n'
                                                        '      protocol\r\n'
                                                        '      screenshot_urls {\r\n'
                                                        '        file\r\n'
                                                        '        id\r\n'
                                                        '        medium_thumb\r\n'
                                                        '        small_thumb\r\n'
                                                        '        __typename\r\n'
                                                        '      }\r\n'
                                                        '      src\r\n'
                                                        '      type\r\n'
                                                        '      __typename\r\n'
                                                        '    }\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '  __typename\r\n'
                                                        '}',
                                       'method': 'POST',
                                       'method_name': 'finding_update',
                                       'name': 'FindingUpdate',
                                       'path': '/graphql'},
                                      {'aliases': [],
                                       'body_mode': 'graphql',
                                       'default_params': [],
                                       'description': '<p>You can create a new report narrative by '
                                                      'passing in a new report narrative object '
                                                      'with a new unique CUID value in the '
                                                      '<code>id</code> property.</p>\n',
                                       'folder_path': ['Graph QL Mutations'],
                                       'graphql_query': 'mutation NarrativeUpdate($clientId: Int!, '
                                                        '$data: [NarrativeInput!]!, $reportId: '
                                                        'Int!, $tenantId: Int!) {\r\n'
                                                        '  narrativeUpdate(\r\n'
                                                        '    clientId: $clientId\r\n'
                                                        '    data: $data\r\n'
                                                        '    reportId: $reportId\r\n'
                                                        '    tenantId: $tenantId\r\n'
                                                        '  ) {\r\n'
                                                        '    ...NarrativeFragment\r\n'
                                                        '    __typename\r\n'
                                                        '  }\r\n'
                                                        '}\r\n'
                                                        '\r\n'
                                                        'fragment NarrativeFragment on Narrative '
                                                        '{\r\n'
                                                        '  id\r\n'
                                                        '  label\r\n'
                                                        '  tags\r\n'
                                                        '  text\r\n'
                                                        '  titleCommentThreadId\r\n'
                                                        '  isFromNarrativesDB\r\n'
                                                        '  __typename\r\n'
                                                        '}',
                                       'method': 'POST',
                                       'method_name': 'narrative_update',
                                       'name': 'NarrativeUpdate',
                                       'path': '/graphql'}]},
 'graph_ql_queries': {'display_name': 'Graph QL Queries',
                      'endpoints': [{'aliases': [],
                                     'body_mode': 'graphql',
                                     'default_params': [],
                                     'description': '',
                                     'folder_path': ['Graph QL Queries'],
                                     'graphql_query': 'query clientAsset ($clientId: ID!, $id: '
                                                      'ID!) {\n'
                                                      '    clientAsset (clientId: $clientId, id: '
                                                      '$id) {\n'
                                                      '        client {\n'
                                                      '            id\n'
                                                      '            name\n'
                                                      '        }\n'
                                                      '        created\n'
                                                      '        description\n'
                                                      '        findings {\n'
                                                      '            id\n'
                                                      '            instances {\n'
                                                      '                report_flaw_title\n'
                                                      '                report_id\n'
                                                      '                report_severity\n'
                                                      '                report_status\n'
                                                      '            }\n'
                                                      '            severity\n'
                                                      '            status\n'
                                                      '            title\n'
                                                      '        }\n'
                                                      '        id\n'
                                                      '        name\n'
                                                      '    }\n'
                                                      '}',
                                     'method': 'POST',
                                     'method_name': 'client_asset',
                                     'name': 'clientAsset',
                                     'path': '/graphql'}]},
 'integrations': {'display_name': 'Integrations',
                  'endpoints': [{'aliases': ['get'],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'TenableIO'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'get_integration',
                                 'name': 'Get Integration',
                                 'path': '/api/v2/tenant/{tenantId}/integrations/{product}'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'TenableIO'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'save_integration',
                                 'name': 'Save Integration',
                                 'path': '/api/v2/tenant/{tenantId}/integrations/{product}'},
                                {'aliases': ['delete'],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'TenableIO'],
                                 'graphql_query': None,
                                 'method': 'DELETE',
                                 'method_name': 'delete_integration',
                                 'name': 'Delete Integration',
                                 'path': '/api/v2/tenant/{tenantId}/integrations/{product}'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'TenableIO'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'tenable_io_get_tags',
                                 'name': 'TenableIO Get Tags',
                                 'path': '/api/v2/integrations/tenable-io/tags'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'TenableIO'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'tenable_io_sync_tags',
                                 'name': 'TenableIO Sync Tags',
                                 'path': '/api/v2/integrations/tenable-io/tags/sync'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '<p>This request <strong>retrieves a list of Jira '
                                                'projects</strong> that are used to associate a '
                                                'finding ticket to**.**</p>\n',
                                 'folder_path': ['Integrations', 'Jira', 'Legacy Integration'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'list_jira_projects',
                                 'name': 'List Jira Projects',
                                 'path': '/api/v1/jira/projects'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p><strong>DEPRECATED</strong>: Will be removed '
                                                'in 2.14</p>\n'
                                                '<p>Use <a '
                                                'href="https://api-docs.plextrac.com/#90ff6d8c-b803-43d0-992f-244d0389e65f">Create '
                                                'Jira Ticket From Findings</a> instead</p>\n'
                                                '<p>This request <strong>creates a finding for a '
                                                'specific report and creates a Jira '
                                                'ticket</strong>, if that integration is '
                                                'configured.</p>\n',
                                 'folder_path': ['Integrations', 'Jira', 'Legacy Integration'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'create_and_link_jira_ticket_to_finding',
                                 'name': 'Create and Link Jira Ticket to Finding',
                                 'path': '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}/createAndLinkJiraTicket'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p><strong>DEPRECATED</strong>: Will be removed '
                                                'in 2.14</p>\n'
                                                '<p>Use <a '
                                                'href="https://api-docs.plextrac.com/#90ff6d8c-b803-43d0-992f-244d0389e65f">Create '
                                                'Jira Ticket From Findings</a> instead</p>\n'
                                                '<p>This request <strong>retrieves findings from a '
                                                'specific report and creates Jira '
                                                'tickets</strong>, if that integration is '
                                                'configured.</p>\n',
                                 'folder_path': ['Integrations', 'Jira', 'Legacy Integration'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'bulk_create_and_link_jira_tickets_to_findings',
                                 'name': 'Bulk Create and Link Jira Tickets to Findings',
                                 'path': '/api/v2/client/{clientId}/report/{reportId}/findings/createJiraTickets'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p><code>syncFrequency</code> must one of '
                                                'following string value:</p>\n'
                                                '<ul>\n'
                                                '<li><p>"Half_Hour"</p>\n'
                                                '</li>\n'
                                                '<li><p>"Hourly"</p>\n'
                                                '</li>\n'
                                                '<li><p>"Daily"</p>\n'
                                                '</li>\n'
                                                '</ul>\n',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'create_jira_connection',
                                 'name': 'Create Jira Connection',
                                 'path': '/api/v2/jira/connect'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p><code>syncFrequency</code> must one of '
                                                'following string value:</p>\n'
                                                '<ul>\n'
                                                '<li><p>"Half_Hour"</p>\n'
                                                '</li>\n'
                                                '<li><p>"Hourly"</p>\n'
                                                '</li>\n'
                                                '<li><p>"Daily"</p>\n'
                                                '</li>\n'
                                                '</ul>\n',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'PUT',
                                 'method_name': 'update_jira_connection',
                                 'name': 'Update Jira Connection',
                                 'path': '/api/v2/jira/connect/{integrationId}'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'DELETE',
                                 'method_name': 'delete_jira_connection',
                                 'name': 'Delete Jira Connection',
                                 'path': '/api/v2/jira/connect/{integrationId}'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p><code>mappingType</code> must be one of '
                                                'following string value:</p>\n'
                                                '<ul>\n'
                                                '<li><p>"Default"</p>\n'
                                                '</li>\n'
                                                '<li><p>"Custom"</p>\n'
                                                '</li>\n'
                                                '</ul>\n',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'set_jira_projects',
                                 'name': 'Set Jira Projects',
                                 'path': '/api/v2/jira/projects/{integrationId}'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'get_jira_projects',
                                 'name': 'Get Jira Projects',
                                 'path': '/api/v2/jira/integration/projects/{integrationId}'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'get_issue_mapping_types',
                                 'name': 'Get Issue Mapping Types',
                                 'path': '/api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'reset_issue_mapping_types',
                                 'name': 'Reset Issue Mapping Types',
                                 'path': '/api/v2/jira/integration/{integrationId}/projects/{jiraProjectId}/issues/{jiraIssueTypeId}/mappings/reset'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'PUT',
                                 'method_name': 'bulk_update_issue_type_mappings',
                                 'name': 'Bulk Update Issue Type Mappings',
                                 'path': '/api/v2/jira/integration/{integrationId}/issues/bulk/mappings'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'create_jira_ticket_from_findings',
                                 'name': 'Create Jira Ticket From Findings',
                                 'path': '/api/v2/jira/integration/{integrationId}/issues/create'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations', 'Jira'],
                                 'graphql_query': None,
                                 'method': 'DELETE',
                                 'method_name': 'unlink_jira_ticket_from_findings',
                                 'name': 'Unlink Jira Ticket From Findings',
                                 'path': '/api/v2/jira/integration/unlink/client/{clientId}/report/{reportId}/finding/{findingId}'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '',
                                 'folder_path': ['Integrations'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'get_configurations',
                                 'name': 'Get Configurations',
                                 'path': '/api/v2/integrations/configurations'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p>Creates a config for an integration.</p>\n'
                                                '<p><code>integrationType</code> can be one '
                                                'of:</p>\n'
                                                '<ul>\n'
                                                '<li>Colbalt</li>\n'
                                                '<li>HackerOne</li>\n'
                                                '<li>MSV</li>\n'
                                                '<li>Snyk</li>\n'
                                                '</ul>\n'
                                                '<p><code>apiUserName</code> and '
                                                '<code>orgId</code> are allowed to be an empty '
                                                "string if they don't exist for your "
                                                'integration.</p>\n',
                                 'folder_path': ['Integrations'],
                                 'graphql_query': None,
                                 'method': 'POST',
                                 'method_name': 'create_configurations',
                                 'name': 'Create Configurations',
                                 'path': '/api/v2/integrations/configurations'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '<p>Creates a config for an integration.</p>\n'
                                                '<p><code>integrationType</code> can be one '
                                                'of:</p>\n'
                                                '<ul>\n'
                                                '<li>Colbalt</li>\n'
                                                '<li>HackerOne</li>\n'
                                                '<li>MSV</li>\n'
                                                '<li>Snyk</li>\n'
                                                '</ul>\n'
                                                '<p><code>apiUserName</code> and '
                                                '<code>orgId</code> are allowed to be an empty '
                                                "string if they don't exist for your "
                                                'integration.</p>\n',
                                 'folder_path': ['Integrations'],
                                 'graphql_query': None,
                                 'method': 'GET',
                                 'method_name': 'get_configuration',
                                 'name': 'Get Configuration',
                                 'path': '/api/v2/integrations/configurations/{configId}'},
                                {'aliases': [],
                                 'body_mode': 'raw',
                                 'default_params': [],
                                 'description': '<p>Creates a config for an integration.</p>\n'
                                                '<p><code>integrationType</code> can be one '
                                                'of:</p>\n'
                                                '<ul>\n'
                                                '<li>Colbalt</li>\n'
                                                '<li>HackerOne</li>\n'
                                                '<li>MSV</li>\n'
                                                '<li>Snyk</li>\n'
                                                '</ul>\n'
                                                '<p><code>apiUserName</code> and '
                                                '<code>orgId</code> are allowed to be an empty '
                                                "string if they don't exist for your "
                                                'integration.</p>\n',
                                 'folder_path': ['Integrations'],
                                 'graphql_query': None,
                                 'method': 'PUT',
                                 'method_name': 'update_configuration',
                                 'name': 'Update Configuration',
                                 'path': '/api/v2/integrations/configurations/{configId}'},
                                {'aliases': [],
                                 'body_mode': 'none',
                                 'default_params': [],
                                 'description': '<p>Creates a config for an integration.</p>\n'
                                                '<p><code>integrationType</code> can be one '
                                                'of:</p>\n'
                                                '<ul>\n'
                                                '<li>Colbalt</li>\n'
                                                '<li>HackerOne</li>\n'
                                                '<li>MSV</li>\n'
                                                '<li>Snyk</li>\n'
                                                '</ul>\n'
                                                '<p><code>apiUserName</code> and '
                                                '<code>orgId</code> are allowed to be an empty '
                                                "string if they don't exist for your "
                                                'integration.</p>\n',
                                 'folder_path': ['Integrations'],
                                 'graphql_query': None,
                                 'method': 'DELETE',
                                 'method_name': 'delete_configuration',
                                 'name': 'Delete Configuration',
                                 'path': '/api/v2/integrations/configurations/{configId}'}]},
 'mailer': {'display_name': 'Mailer',
            'endpoints': [{'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>Get Mailer Templates</p>\n',
                           'folder_path': ['Mailer'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'get_mailer_templates',
                           'name': 'Get Mailer Templates',
                           'path': '/api/v2/tenants/{tenantId}/mailer/templates'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>Get Email Template</p>\n',
                           'folder_path': ['Mailer'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'get_email_template',
                           'name': 'Get Email Template',
                           'path': '/api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD'},
                          {'aliases': [],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '<p>Upsert Email Template</p>\n',
                           'folder_path': ['Mailer'],
                           'graphql_query': None,
                           'method': 'PUT',
                           'method_name': 'upsert_email_template',
                           'name': 'Upsert Email Template',
                           'path': '/api/v2/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD'}]},
 'parser_actions': {'display_name': 'Parser Actions',
                    'endpoints': [{'aliases': [],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>enable or disable global mapping of scanner '
                                                  'findings to writeups</p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'POST',
                                   'method_name': 'enable_disable_parser_plugin_actions',
                                   'name': 'Enable/Disable Parser Plugin Actions',
                                   'path': '/api/v1/tenant/{tenantId}/integrationconfig/parserConfig'},
                                  {'aliases': [],
                                   'body_mode': 'none',
                                   'default_params': [],
                                   'description': '<p>This request retrieves <strong>a list of '
                                                  'available parsers</strong>.</p>\n'
                                                  '<p>Returned source field can be used for '
                                                  'endpoints requiring '
                                                  '<code>parserId</code>.</p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'GET',
                                   'method_name': 'get_tenant_parsers',
                                   'name': 'Get Tenant Parsers',
                                   'path': '/api/v1/tenant/{tenantId}/actions'},
                                  {'aliases': [],
                                   'body_mode': 'none',
                                   'default_params': [('limit', '985'),
                                                      ('skip', '0'),
                                                      ('type', 'DEFAULT'),
                                                      ('query', 'sql')],
                                   'description': '<p>This request retrieves <strong>a list of '
                                                  'parser actions for a tenant</strong> per '
                                                  'identified parser source**.**</p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'GET',
                                   'method_name': 'get_tenant_parser_actions',
                                   'name': 'Get Tenant Parser Actions',
                                   'path': '/api/v1/tenant/{tenantId}/actions/{parserName}'},
                                  {'aliases': [],
                                   'body_mode': 'none',
                                   'default_params': [],
                                   'description': '',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'GET',
                                   'method_name': 'get_tenant_parser_action',
                                   'name': 'Get Tenant Parser Action',
                                   'path': '/api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}'},
                                  {'aliases': [],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>This request <strong>creates a parser action '
                                                  'for a tenant.</strong></p>\n'
                                                  '<p>Required fields: <code>id</code>, '
                                                  '<code>severity</code>, <code>title</code></p>\n'
                                                  '<p><code>action</code> field: DEFAULT, LINK, '
                                                  'IGNORE</p>\n'
                                                  '<p><code>action</code> field defaults to '
                                                  'DEFAULT when not supplied.</p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'POST',
                                   'method_name': 'create_tenant_parser_action',
                                   'name': 'Create Tenant Parser Action',
                                   'path': '/api/v1/tenant/{tenantId}/actions/{parserName}/action'},
                                  {'aliases': ['update'],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>This request <strong>updates a specific '
                                                  'parser and specific action for a '
                                                  'tenant.</strong></p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'PUT',
                                   'method_name': 'update_parser_action',
                                   'name': 'Update Parser Action',
                                   'path': '/api/v1/tenant/{tenantId}/actions/{parserName}/action/{actionId}'},
                                  {'aliases': [],
                                   'body_mode': 'raw',
                                   'default_params': [],
                                   'description': '<p>This request <strong>bulk</strong> '
                                                  '<strong>updates a specific parser and specific '
                                                  'action for a tenant.</strong></p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'PUT',
                                   'method_name': 'bulk_update_tenant_parser_actions',
                                   'name': 'Bulk Update Tenant Parser Actions',
                                   'path': '/api/v1/tenant/{tenantId}/actions/{parserName}/bulk'},
                                  {'aliases': [],
                                   'body_mode': 'formdata',
                                   'default_params': [],
                                   'description': '<p>Used to import parser actions into a parser '
                                                  'from a scan file. Scan files are imported '
                                                  'directly to the parser and not into a '
                                                  'report.</p>\n'
                                                  '<p>List of <code>source</code> options:</p>\n'
                                                  '<p>acunetix<br />burp<br />burphtml<br '
                                                  '/>checkmarx<br />coreimpact<br />custom<br '
                                                  '/>hclappscan<br />horizon<br />invicti<br '
                                                  '/>nessus<br />netsparker<br />nexpose<br '
                                                  '/>nipper<br />nmap<br />nodeware<br '
                                                  '/>nodezero<br />openvas<br />owaspzap<br '
                                                  '/>pentera<br />qualys<br />rapidfire<br '
                                                  '/>scythe<br />veracode</p>\n',
                                   'folder_path': ['Parser Actions'],
                                   'graphql_query': None,
                                   'method': 'POST',
                                   'method_name': 'import_parser_plugins',
                                   'name': 'Import Parser Plugins',
                                   'path': '/api/v1/tenant/{tenantId}/actions/upload/{source}'}]},
 'qa_workflow': {'display_name': 'QA Workflow', 'endpoints': []},
 'reports': {'display_name': 'Reports',
             'endpoints': [{'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request <strong>retrieves a count</strong> of '
                                           'the number of occurrences that exist in a report for a '
                                           'given query. This will not result in any changes of '
                                           'data but only return a numerical value.</p>\n'
                                           '<p>The <code>instanceUrl</code> and desired query '
                                           'field is needed to execute the call.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>confirmation of query success</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>count</td>\n'
                                           '<td>the number of occurrences that exist in a '
                                           'report</td>\n'
                                           '<td>41</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports', 'Search & Replace'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'count_report_search_occurrences',
                            'name': 'Search & Replace in Report (Occurrences)',
                            'path': '/api/v1/search-replace/occurrences'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request <strong>finds and replaces</strong> a '
                                           'value in a report, such a report title, finding title, '
                                           'or field key.</p>\n'
                                           '<p><strong>NOTE:</strong> This call can effect how a '
                                           'Jinja template will interact with the report if labels '
                                           'and keys are changed.</p>\n'
                                           '<p>The <code>instanceUrl</code> and desired query '
                                           'field is needed to execute the call.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>confirmation of query success</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>data</td>\n'
                                           '<td>was the data found and replaced</td>\n'
                                           '<td>true</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports', 'Search & Replace'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'replace_report_text',
                            'name': 'Search & Replace in Report (Replace)',
                            'path': '/api/v1/search-replace'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request <strong>retrieves</strong> a list of '
                                           'reports for a specific client. The information '
                                           'retrieved is limited and intended to provide an '
                                           'overview of the number of reports for a client.</p>\n'
                                           '<p>A successful call returns a List of JSON objects '
                                           'with summarized information about each report.</p>\n'
                                           '<p>Below is the structure of the summarized JSON '
                                           'returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>id</td>\n'
                                           '<td>report ID and client ID combined</td>\n'
                                           '<td>report_500004_client_4155</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>doc_id</td>\n'
                                           '<td>List with a single value of client ID</td>\n'
                                           '<td>[4155]</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>data</td>\n'
                                           '<td>List of information about the report. See table '
                                           'below.</td>\n'
                                           '<td>[500004, "Karbo Industries", null, "Draft", 1, '
                                           '["<a '
                                           'href="mailto:test.operator@email.com">test.operator@email.com</a>"], '
                                           '["<a '
                                           'href="mailto:test.reviewer@email.com">test.reviewer@email.com</a>"], '
                                           '1680796600582, "2020-08-01T08:00:00.000000Z", '
                                           '"2020-08-01T08:00:00.000000Z", [ "report_tag" ], '
                                           '"default", "default"]</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div><p><code>data</code> Array Values</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>data</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>Report ID</td>\n'
                                           '<td>integer of report ID</td>\n'
                                           '<td>500007</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Name</td>\n'
                                           '<td>string of report name</td>\n'
                                           '<td>Test Report</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Null Value</td>\n'
                                           '<td>A null value is inserted to maintain ordering for '
                                           'legacy implementations, from when a value was '
                                           'removed.</td>\n'
                                           '<td>null</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Status</td>\n'
                                           '<td>string of report status</td>\n'
                                           '<td>Draft</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Findings Count</td>\n'
                                           '<td>integer of findings in the report</td>\n'
                                           '<td>15</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Operators</td>\n'
                                           '<td>list of emails for all users assigned as a report '
                                           'operator</td>\n'
                                           '<td>["<a '
                                           'href="mailto:example.email@plextrac.com">example.email@plextrac.com</a>"]</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Reviewers</td>\n'
                                           '<td>list of emails for all users assigned as a report '
                                           'reviewers</td>\n'
                                           '<td>["<a '
                                           'href="mailto:example.email@plextrac.com">example.email@plextrac.com</a>"]</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Created At Date</td>\n'
                                           '<td>integer of milliseconds since Epoch when the '
                                           'report was created</td>\n'
                                           '<td>1678135873086</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Start Date</td>\n'
                                           '<td>string of report start date</td>\n'
                                           '<td>2020-08-01T08:00:00.000000Z</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>End Date</td>\n'
                                           '<td>string of report end date</td>\n'
                                           '<td>2020-08-31T08:00:00.000000Z</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Tags</td>\n'
                                           '<td>list of report tags</td>\n'
                                           '<td>[ "report_tag" ]</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Report Template Name</td>\n'
                                           '<td>string name of selected report template</td>\n'
                                           '<td>default</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>Findings Layout Name</td>\n'
                                           '<td>string name of selected findings layout</td>\n'
                                           '<td>default</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'list_client_reports',
                            'name': 'List Client Reports',
                            'path': '/api/v1/client/{clientId}/reports'},
                           {'aliases': ['list'],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request <strong>retrieves a list of '
                                           'reports</strong> for a tenant.</p>\n'
                                           '<p><code>pagination</code> is a required key while '
                                           '<code>sort</code> and <code>filters</code> are '
                                           'optional.</p>\n'
                                           '<p>The <code>pagination.limit</code> must be one of '
                                           '[5, 10, 25, 50, 100, 1000]. The '
                                           '<code>pagination.offset</code> is the number of '
                                           'records to shift by, not the number of pages to shift '
                                           'by. i.e. offset 2, limit 10 gives you records 2-12 not '
                                           '20-30</p>\n'
                                           '<p>The following values can be used in the '
                                           '<code>filters.by</code> field:</p>\n'
                                           '<ul>\n'
                                           '<li><p>name</p>\n'
                                           '</li>\n'
                                           '<li><p>reviewers (array[str] of reviewer emails)</p>\n'
                                           '</li>\n'
                                           '<li><p>operators(array[str] of operator emails)</p>\n'
                                           '</li>\n'
                                           '<li><p>clients (array[int] of client IDs a report is '
                                           'under)</p>\n'
                                           '</li>\n'
                                           '<li><p>status (array[str] of report statuses)</p>\n'
                                           '</li>\n'
                                           '<li><p>cuids (array of CUID strings for specific '
                                           'reports)</p>\n'
                                           '</li>\n'
                                           '</ul>\n'
                                           '<p>The following values can be used in the '
                                           '<code>sort.by</code> field:</p>\n'
                                           '<ul>\n'
                                           '<li><p>name</p>\n'
                                           '</li>\n'
                                           '<li><p>status</p>\n'
                                           '</li>\n'
                                           '</ul>\n'
                                           '<p>The following values can be used in the '
                                           '<code>sort.order</code> field:</p>\n'
                                           '<ul>\n'
                                           '<li><p>ASC</p>\n'
                                           '</li>\n'
                                           '<li><p>DESC</p>\n'
                                           '</li>\n'
                                           '</ul>\n'
                                           '<p><strong>Filter by Report CUID</strong></p>\n'
                                           '<p>Example payload section to filter by report CUID. '
                                           'Can only supply one CUID to get a single report.</p>\n'
                                           '<pre class="click-to-expand-wrapper '
                                           'is-snippet-wrapper"><code>"filters": [\n'
                                           '    {\n'
                                           '        "by": "cuids", "value": [\n'
                                           '            "cm6tr8ph50000356mz4xel5e7",\n'
                                           '            "cm6tr8z6j0001356mhmdddklw",\n'
                                           '            "cm6tr92qk0002356mejik0zpg"\n'
                                           '        ]\n'
                                           '    }\n'
                                           ']\n'
                                           '\n'
                                           '</code></pre>',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'list_reports',
                            'name': 'Get Report List',
                            'path': '/api/v2/reports'},
                           {'aliases': ['get'],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request <strong>retrieves</strong> a specific '
                                           'report for a client and provides robust information '
                                           'about the report.</p>\n'
                                           '<p>The <code>instanceUrl</code>, '
                                           '<code>reportId,</code> and <code>clientId</code> is '
                                           'needed to execute the call.</p>\n'
                                           '<p>A successful call returns the JSON object of the '
                                           'report stored in the DB. See <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/report-object">Report '
                                           'Object</a> for details on how this JSON is '
                                           'structured</p>\n'
                                           '<p><strong>Required RBAC Permissions:</strong></p>\n'
                                           '<ul>\n'
                                           '<li><code>View Reports</code></li>\n'
                                           '</ul>\n'
                                           '<p>This only returns <strong>Published</strong> '
                                           'reports, unless the user also has the <code>Ability to '
                                           'mark a finding as published</code> permission.</p>\n',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'get_report',
                            'name': 'Get Report',
                            'path': '/api/v1/client/{clientId}/report/{reportId}'},
                           {'aliases': ['create'],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request <strong>creates</strong> a report for '
                                           'a client.</p>\n'
                                           '<p>The <code>instanceUrl</code>and '
                                           '<code>clientId</code> is needed to execute.</p>\n'
                                           '<p>In addition to the example below, see <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/report-object">Report '
                                           'Object</a> for details on the payload structure.</p>\n'
                                           '<p><strong>Note:</strong> The fields listed in the '
                                           'example should be the only fields added to the request '
                                           'during creation. Other fields that can be present on a '
                                           'report can be added using <a '
                                           'href="https://api-docs.plextrac.com/#51a2090c-ced1-46b0-bfac-8ed6bcd03457">PUT '
                                           'Update Report</a> after the report is created.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>message</td>\n'
                                           '<td>status of task</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>doc_id</td>\n'
                                           '<td>new report ID combined with client ID</td>\n'
                                           '<td>report_500006_client_4155</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>report_id</td>\n'
                                           '<td>report ID</td>\n'
                                           '<td>500006</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'create_report',
                            'name': 'Create Report',
                            'path': '/api/v1/client/{clientId}/report/create'},
                           {'aliases': ['update'],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>This request <strong>updates</strong> a report. '
                                           'This does not update/relate to the findings on a '
                                           'report.</p>\n'
                                           '<p>The <code>instanceUrl</code>, '
                                           '<code>reportId,</code> and <code>clientId</code> is '
                                           'needed to execute the call.</p>\n'
                                           '<p>In addition to the example below, see <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/report-object">Report '
                                           'Object</a> for details on the payload structure.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>status of change update</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>message</td>\n'
                                           '<td>change message</td>\n'
                                           '<td>Report Updated Successfully</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>data</td>\n'
                                           '<td>the JSON of the updated report stored in the '
                                           'DB</td>\n'
                                           '<td></td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'PUT',
                            'method_name': 'update_report',
                            'name': 'Update Report',
                            'path': '/api/v1/client/{clientId}/report/{reportId}'},
                           {'aliases': ['delete'],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request <strong>removes</strong> a report for '
                                           'a client.</p>\n'
                                           '<p>The <code>instanceUrl</code> '
                                           ',<code>clientId,</code> and <code>reportId</code> is '
                                           'needed to execute the call.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>status</td>\n'
                                           '<td>validation of request</td>\n'
                                           '<td>success</td>\n'
                                           '</tr>\n'
                                           '<tr>\n'
                                           '<td>data</td>\n'
                                           '<td>further validation</td>\n'
                                           '<td>true</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'DELETE',
                            'method_name': 'delete_report',
                            'name': 'Delete Report',
                            'path': '/api/v1/client/{clientId}/report/{reportId}'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'bulk_delete_reports',
                            'name': 'Bulk Delete Reports',
                            'path': '/api/v2/reports/bulk/delete'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request <strong>retrieves</strong> an exhibit '
                                           'filename from a specific report.</p>\n'
                                           '<p>The <code>instanceUrl</code> '
                                           ',<code>clientId,</code> <code>reportId,</code> and '
                                           '<code>exhibitId</code> is needed to execute.</p>\n'
                                           '<p>Below is returned on a successful call:</p>\n'
                                           '<div class="click-to-expand-wrapper '
                                           'is-table-wrapper"><table>\n'
                                           '<thead>\n'
                                           '<tr>\n'
                                           '<th><strong>parameter</strong></th>\n'
                                           '<th><strong>definition</strong></th>\n'
                                           '<th><strong>example value</strong></th>\n'
                                           '</tr>\n'
                                           '</thead>\n'
                                           '<tbody>\n'
                                           '<tr>\n'
                                           '<td>id</td>\n'
                                           '<td>filename of exhibit</td>\n'
                                           '<td>2430ffd3-0c48-4adf-b211-d960ed06176d.png</td>\n'
                                           '</tr>\n'
                                           '</tbody>\n'
                                           '</table>\n'
                                           '</div>',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'get_report_exhibit',
                            'name': 'Get Exhibit',
                            'path': '/api/v1/client/{clientId}/report/{reportId}/{exhibitId}'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'bulk_add_tags_to_reports',
                            'name': 'Bulk Add Tags to Report',
                            'path': '/api/v2/reports/bulk/tags'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>The reviewer email must match an existing PT user '
                                           'email.</p>\n',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'bulk_assign_reviewers_to_reports',
                            'name': 'Bulk Assign Reviewers to Report',
                            'path': '/api/v2/reports/bulk/reviewers'},
                           {'aliases': [],
                            'body_mode': 'raw',
                            'default_params': [],
                            'description': '<p>The reviewer email must match an existing PT user '
                                           'email.</p>\n',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'bulk_update_report_statuses',
                            'name': 'Bulk Adjust Status of Report',
                            'path': '/api/v2/reports/bulk/status'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [],
                            'description': '<p>This request <strong>exports a report</strong> in '
                                           'ptrac format for further manipulation and future '
                                           'importing back into PlexTrac.</p>\n'
                                           '<p>The <code>instanceUrl</code> '
                                           ',<code>clientId,</code> and <code>reportId</code> is '
                                           'needed to execute.</p>\n',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'export_report_to_ptrac',
                            'name': 'Export Report to Ptrac',
                            'path': '/api/v1/client/{clientId}/report/{reportId}/export/ptrac'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [('includeEvidence', 'false')],
                            'description': '<p>This requests <strong>exports a PlexTrac</strong> '
                                           '<strong>report to Word</strong> (.docx).</p>\n'
                                           '<p><strong>Important</strong>: Be aware that setting '
                                           '<code>includeEvidence</code> to <code>true</code> will '
                                           'result in long export times due to handling extra '
                                           'data. Set to <code>false</code> unless evidence is '
                                           'required at export.</p>\n'
                                           '<p>The endpoint needs the report data and Jinja2 coded '
                                           'Word .docx file (Export Template) that will be '
                                           'populated with data.</p>\n'
                                           '<p>If the Report Template field in a report is '
                                           'selected, that report already has a reference to the '
                                           'Jinja2 Export Template (Word). If not, add the '
                                           'additional <code>templateID</code> query parameter. '
                                           'This is the ID of a previously uploaded Export '
                                           'Template (Word). See the List Export Templates '
                                           'endpoint for more info about retrieving this ID.</p>\n'
                                           '<p>More information on <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/product-documentation/reports/export-report">exporting '
                                           'a report</a> can be found on the PlexTrac Product '
                                           'Documentation site.</p>\n',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'export_report_to_word',
                            'name': 'Export Report to Word',
                            'path': '/api/v1/client/{clientId}/report/{reportId}/export/doc'},
                           {'aliases': [],
                            'body_mode': 'none',
                            'default_params': [('includeEvidence', 'false')],
                            'description': '<p>This requests <strong>exports a PlexTrac</strong> '
                                           '<strong>report to a PDF</strong>.</p>\n'
                                           '<p><strong>Important</strong>: Be aware that setting '
                                           '<code>includeEvidence</code> to <code>true</code> will '
                                           'result in long export times due to handling extra '
                                           'data. Set to <code>false</code> unless evidence is '
                                           'required at export.</p>\n'
                                           '<p>The endpoint needs the report data and Jinja2 coded '
                                           'HTML .j2 file (Export Template) that will be populated '
                                           'with data.</p>\n'
                                           '<p>If the Report Template field in a report is '
                                           'selected, that report already has a reference to the '
                                           'PDF Export Template. If not, add the additional '
                                           '<code>templateID</code> query parameter. This is the '
                                           'ID of a previously uploaded Export Template (PDF). See '
                                           'the List Export Templates endpoint for more info about '
                                           'retrieving this ID.</p>\n'
                                           '<p>More information on <a '
                                           'href="https://docs.plextrac.com/plextrac-documentation/product-documentation/reports/export-report">exporting '
                                           'a report</a> can be found on the PlexTrac Product '
                                           'Documentation site.</p>\n',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'GET',
                            'method_name': 'export_report_to_pdf',
                            'name': 'Export Report to PDF',
                            'path': '/api/v1/client/{clientId}/report/{reportId}/export/pdf'},
                           {'aliases': [],
                            'body_mode': 'formdata',
                            'default_params': [],
                            'description': '',
                            'folder_path': ['Reports'],
                            'graphql_query': None,
                            'method': 'POST',
                            'method_name': 'import_report_from_ptrac',
                            'name': 'Import Ptrac Report',
                            'path': '/api/v1/client/{clientId}/report/import'}]},
 'runbooks': {'display_name': 'Runbooks',
              'endpoints': [{'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Operators'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureOperatorListV2($procedureId: '
                                              'ID!) {\r\n'
                                              '  '
                                              'runbookEngagementProcedureOperatorListV2(procedureId: '
                                              '$procedureId) {\r\n'
                                              '    ...RunbookEngagementProcedureOperatorV2Data\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureOperatorV2Data '
                                              'on RunbookEngagementProcedureOperatorV2 {\r\n'
                                              '  id\r\n'
                                              '  userId\r\n'
                                              '  team\r\n'
                                              '  createdAt\r\n'
                                              '  user {\r\n'
                                              '    id\r\n'
                                              '    fullName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_operator_list',
                             'name': 'RunbookEngagementProcedureOperatorListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Assign a user as an operator to a procedure in a '
                                            'RunbookV2 engagement.</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Operators'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureOperatorsUpdateV2($procedureId: '
                                              'ID!, $operators: '
                                              '[RunbookEngagementProcedureOperatorInputV2!]!) {\r\n'
                                              '  runbookEngagementProcedureOperatorsUpdateV2(\r\n'
                                              '    procedureId: $procedureId\r\n'
                                              '    operators: $operators\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementProcedureOperatorV2Data\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureOperatorV2Data '
                                              'on RunbookEngagementProcedureOperatorV2 {\r\n'
                                              '  id\r\n'
                                              '  userId\r\n'
                                              '  team\r\n'
                                              '  createdAt\r\n'
                                              '  user {\r\n'
                                              '    id\r\n'
                                              '    fullName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_operators_update',
                             'name': 'RunbookEngagementProcedureOperatorsUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Targeted Assets'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureAssetListV2($procedureId: '
                                              'ID!) {\r\n'
                                              '  '
                                              'runbookEngagementProcedureAssetListV2(procedureId: '
                                              '$procedureId) {\r\n'
                                              '    ...RunbookEngagementProcedureAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureAssetDataV2 on '
                                              'RunbookEngagementProcedureAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  includeInFinding\r\n'
                                              '  outcomeBlue\r\n'
                                              '  outcomeRed\r\n'
                                              '  clientAsset {\r\n'
                                              '    ...ClientAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  evidences {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureAssetEvidenceDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ClientAssetDataV2 on ClientAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  parentAssetId\r\n'
                                              '  parentAsset {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  type\r\n'
                                              '  criticality\r\n'
                                              '  knownIps\r\n'
                                              '  tags\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureAssetEvidenceDataV2 on '
                                              'RunbookEngagementProcedureAssetEvidenceV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_asset_list',
                             'name': 'RunbookEngagementProcedureAssetListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Add an existing asset to a procedure in a '
                                            'RunbookV2 engagement.</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Targeted Assets'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureAssetsAddV2($procedureId: '
                                              'ID!, $clientAssetIds: [ID!]!) {\r\n'
                                              '  runbookEngagementProcedureAssetsAddV2(\r\n'
                                              '    procedureId: $procedureId\r\n'
                                              '    clientAssetIds: $clientAssetIds\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementProcedureAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureAssetDataV2 on '
                                              'RunbookEngagementProcedureAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  includeInFinding\r\n'
                                              '  outcomeBlue\r\n'
                                              '  outcomeRed\r\n'
                                              '  clientAsset {\r\n'
                                              '    ...ClientAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  evidences {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureAssetEvidenceDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ClientAssetDataV2 on ClientAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  parentAssetId\r\n'
                                              '  parentAsset {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  type\r\n'
                                              '  criticality\r\n'
                                              '  knownIps\r\n'
                                              '  tags\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureAssetEvidenceDataV2 on '
                                              'RunbookEngagementProcedureAssetEvidenceV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_assets_add',
                             'name': 'RunbookEngagementProcedureAssetsAddV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Create a new asset and add it to a procedure in a '
                                            'RunbookV2 engagement.</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Targeted Assets'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureAssetCreateV2($procedureId: '
                                              'ID!, $clientAsset: ClientAssetCreateInputV2!, '
                                              '$evidences: '
                                              '[RunbookEngagementProcedureAssetEvidenceCreateInputV2!]) '
                                              '{\r\n'
                                              '  runbookEngagementProcedureAssetCreateV2(\r\n'
                                              '    procedureId: $procedureId\r\n'
                                              '    clientAsset: $clientAsset\r\n'
                                              '    evidences: $evidences\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementProcedureAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureAssetDataV2 on '
                                              'RunbookEngagementProcedureAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  includeInFinding\r\n'
                                              '  outcomeBlue\r\n'
                                              '  outcomeRed\r\n'
                                              '  clientAsset {\r\n'
                                              '    ...ClientAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  evidences {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureAssetEvidenceDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ClientAssetDataV2 on ClientAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  parentAssetId\r\n'
                                              '  parentAsset {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  type\r\n'
                                              '  criticality\r\n'
                                              '  knownIps\r\n'
                                              '  tags\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureAssetEvidenceDataV2 on '
                                              'RunbookEngagementProcedureAssetEvidenceV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_asset_create',
                             'name': 'RunbookEngagementProcedureAssetCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Targeted Assets'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureAssetDeleteV2($id: ID!, '
                                              '$procedureId: ID!) {\r\n'
                                              '  runbookEngagementProcedureAssetDeleteV2(id: $id, '
                                              'procedureId: $procedureId)\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_asset_delete',
                             'name': 'RunbookEngagementProcedureAssetDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Targeted Assets'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureAssetUpdateV2($id: ID!, '
                                              '$procedureId: ID!, $clientAsset: '
                                              'ClientAssetUpdateInputV2, $evidences: '
                                              'RunbookEngagementProcedureAssetEvidencesInputV2, '
                                              '$input: RunbookEngagementProcedureAssetInputV2) '
                                              '{\r\n'
                                              '  runbookEngagementProcedureAssetUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    procedureId: $procedureId\r\n'
                                              '    clientAsset: $clientAsset\r\n'
                                              '    evidences: $evidences\r\n'
                                              '    input: $input\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementProcedureAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureAssetDataV2 on '
                                              'RunbookEngagementProcedureAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  includeInFinding\r\n'
                                              '  outcomeBlue\r\n'
                                              '  outcomeRed\r\n'
                                              '  clientAsset {\r\n'
                                              '    ...ClientAssetDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  evidences {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureAssetEvidenceDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ClientAssetDataV2 on ClientAssetV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  parentAssetId\r\n'
                                              '  parentAsset {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  type\r\n'
                                              '  criticality\r\n'
                                              '  knownIps\r\n'
                                              '  tags\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureAssetEvidenceDataV2 on '
                                              'RunbookEngagementProcedureAssetEvidenceV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_asset_update',
                             'name': 'RunbookEngagementProcedureAssetUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Procedure Logs'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureLogsV2($engagementProcedureId: '
                                              'ID!) {\r\n'
                                              '  '
                                              'runbookEngagementProcedureLogsV2(engagementProcedureId: '
                                              '$engagementProcedureId) {\r\n'
                                              '    ...RunbookEngagementProcedureLogDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureLogDataV2 on '
                                              'RunbookEngagementProcedureLogV2 {\r\n'
                                              '  id\r\n'
                                              '  engagementProcedureId\r\n'
                                              '  text\r\n'
                                              '  startDate\r\n'
                                              '  endDate\r\n'
                                              '  team\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_logs',
                             'name': 'RunbookEngagementProcedureLogsV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Procedure Logs'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureLogCreateV2($engagementProcedureId: '
                                              'ID!, $input: '
                                              'RunbookEngagementProcedureLogCreateInputV2!) {\r\n'
                                              '  runbookEngagementProcedureLogCreateV2(\r\n'
                                              '    engagementProcedureId: '
                                              '$engagementProcedureId\r\n'
                                              '    input: $input\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementProcedureLogDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureLogDataV2 on '
                                              'RunbookEngagementProcedureLogV2 {\r\n'
                                              '  id\r\n'
                                              '  engagementProcedureId\r\n'
                                              '  text\r\n'
                                              '  startDate\r\n'
                                              '  endDate\r\n'
                                              '  team\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_log_create',
                             'name': 'RunbookEngagementProcedureLogCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Procedure Logs'],
                             'graphql_query': 'mutation RunbookEngagementProcedureLogUpdateV2($id: '
                                              'ID!, $input: '
                                              'RunbookEngagementProcedureLogUpdateInputV2!) {\r\n'
                                              '  runbookEngagementProcedureLogUpdateV2(id: $id, '
                                              'input: $input) {\r\n'
                                              '    ...RunbookEngagementProcedureLogDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureLogDataV2 on '
                                              'RunbookEngagementProcedureLogV2 {\r\n'
                                              '  id\r\n'
                                              '  engagementProcedureId\r\n'
                                              '  text\r\n'
                                              '  startDate\r\n'
                                              '  endDate\r\n'
                                              '  team\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_log_update',
                             'name': 'RunbookEngagementProcedureLogUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>team can be one of "RED", "BLUE"</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Procedure Logs'],
                             'graphql_query': 'mutation RunbookEngagementProcedureLogDeleteV2($id: '
                                              'ID!) {\r\n'
                                              '  runbookEngagementProcedureLogDeleteV2(id: $id) '
                                              '{\r\n'
                                              '    ...RunbookEngagementProcedureLogDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureLogDataV2 on '
                                              'RunbookEngagementProcedureLogV2 {\r\n'
                                              '  id\r\n'
                                              '  engagementProcedureId\r\n'
                                              '  text\r\n'
                                              '  startDate\r\n'
                                              '  endDate\r\n'
                                              '  team\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_log_delete',
                             'name': 'RunbookEngagementProcedureLogDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>team can be one of "RED", "BLUE"</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Attachments'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureAttachmentListV2($procedureId: '
                                              'ID!, $team: Team!) {\r\n'
                                              '  runbookEngagementProcedureAttachmentListV2(\r\n'
                                              '    procedureId: $procedureId\r\n'
                                              '    team: $team\r\n'
                                              '  ) {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureAttachmentDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureAttachmentDataV2 '
                                              'on RunbookEngagementProcedureAttachmentV2 {\r\n'
                                              '  id\r\n'
                                              '  team\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  includeInFinding\r\n'
                                              '  filename\r\n'
                                              '  downloadUrl\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_attachment_list',
                             'name': 'RunbookEngagementProcedureAttachmentListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'formdata',
                             'default_params': [],
                             'description': '<p>REST endpoint to upload attachments to a '
                                            'RunbooksV2 Engagment Procedure</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Attachments'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'upload_attachment_to_engagement_procedure',
                             'name': 'Upload Attachment to Engagement Procedure',
                             'path': '/api/v2/runbooks/engagement-procedures/{engagementProcedureId}/attachments/upload'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Attachments'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureAttachmentsUpdateV2($procedureId: '
                                              'ID!, $attachments: '
                                              '[RunbookEngagementProcedureAttachmentInputV2!]!) '
                                              '{\r\n'
                                              '  runbookEngagementProcedureAttachmentsUpdateV2(\r\n'
                                              '    procedureId: $procedureId\r\n'
                                              '    input: $attachments\r\n'
                                              '  ) {\r\n'
                                              '    id\r\n'
                                              '    title\r\n'
                                              '    description\r\n'
                                              '    includeInFinding\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_attachments_update',
                             'name': 'RunbookEngagementProcedureAttachmentsUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures',
                                             'Attachments'],
                             'graphql_query': 'mutation '
                                              'RunbookEngagementProcedureAttachmentDeleteV2($procedureId: '
                                              'ID!, $id: ID!) {\r\n'
                                              '  '
                                              'runbookEngagementProcedureAttachmentDeleteV2(procedureId: '
                                              '$procedureId, id: $id)\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_attachment_delete',
                             'name': 'RunbookEngagementProcedureAttachmentDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureIdsV2($engagementId: ID!) '
                                              '{\r\n'
                                              '  runbookEngagementV2(id: $engagementId) {\r\n'
                                              '    id\r\n'
                                              '    title\r\n'
                                              '    clientId\r\n'
                                              '    procedureIds\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_ids',
                             'name': 'RunbookEngagementProcedureIdsV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureListV2($engagementId: '
                                              'ID!, $args: ListArgs!) {\r\n'
                                              '  runbookEngagementProcedureListV2(engagementId: '
                                              '$engagementId, args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookEngagementProcedureListDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureListDataV2 on '
                                              'RunbookEngagementProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  tenantId\r\n'
                                              '  clientId\r\n'
                                              '  engagementId\r\n'
                                              '  procedureId\r\n'
                                              '  description\r\n'
                                              '  outcomeRed\r\n'
                                              '  outcomeBlue\r\n'
                                              '  status\r\n'
                                              '  attackSource\r\n'
                                              '  notesRed\r\n'
                                              '  notesBlue\r\n'
                                              '  findingSeverity\r\n'
                                              '  runbookProcedure {\r\n'
                                              '    id\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_list',
                             'name': 'RunbookEngagementProcedureListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures'],
                             'graphql_query': 'query '
                                              'RunbookEngagementProcedureDetailV2($procedureId: '
                                              'ID!) {\r\n'
                                              '  runbookEngagementProcedureV2(id: $procedureId) '
                                              '{\r\n'
                                              '    ...RunbookEngagementProcedureDetailV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureDetailV2 on '
                                              'RunbookEngagementProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  status\r\n'
                                              '  outcomeRed\r\n'
                                              '  outcomeBlue\r\n'
                                              '  notesRed\r\n'
                                              '  notesBlue\r\n'
                                              '  attackSource\r\n'
                                              '  findingSeverity\r\n'
                                              '  executionSteps {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureDetailExecutionStep\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  runbookProcedure {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureDetailProcedureDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureDetailExecutionStep on '
                                              'RunbookEngagementProcedureExecutionStep {\r\n'
                                              '  id\r\n'
                                              '  description\r\n'
                                              '  successCriteria\r\n'
                                              '  isCompleted\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureDetailProcedureDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  repository {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureDetailTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    '
                                              '...RunbookEngagementProcedureDetailTacticDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureDetailTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureDetailTacticDataV2 on '
                                              'RunbookTacticV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_detail',
                             'name': 'RunbookEngagementProcedureDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures'],
                             'graphql_query': 'mutation RunbookEngagementProcedureUpdateV2($id: '
                                              'ID!, $data: '
                                              'RunbookEngagementProcedureUpdateInputV2!, '
                                              '$executionSteps: '
                                              'RunbookEngagementProcedureExecutionStepsInputV2, '
                                              '$assets: '
                                              '[RunbookEngagementProcedureAssetUpdateInputV2!]!) '
                                              '{\r\n'
                                              '  runbookEngagementProcedureUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    input: $data\r\n'
                                              '    executionSteps: $executionSteps\r\n'
                                              '  ) {\r\n'
                                              '    id\r\n'
                                              '    status\r\n'
                                              '    outcomeRed\r\n'
                                              '    outcomeBlue\r\n'
                                              '    notesRed\r\n'
                                              '    notesBlue\r\n'
                                              '    attackSource\r\n'
                                              '    findingSeverity\r\n'
                                              '    executionSteps {\r\n'
                                              '      '
                                              '...RunbookEngagementProcedureDetailExecutionStep\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  '
                                              'runbookEngagementProcedureAssetsUpdateV2(procedureId: '
                                              '$id, input: $assets) {\r\n'
                                              '    id\r\n'
                                              '    outcomeBlue\r\n'
                                              '    outcomeRed\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment '
                                              'RunbookEngagementProcedureDetailExecutionStep on '
                                              'RunbookEngagementProcedureExecutionStep {\r\n'
                                              '  id\r\n'
                                              '  description\r\n'
                                              '  successCriteria\r\n'
                                              '  isCompleted\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_update',
                             'name': 'RunbookEngagementProcedureUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'Engagements',
                                             'Engagement Procedures'],
                             'graphql_query': 'mutation RunbookEngagementProcedureDeleteV2($id: '
                                              'ID!) {\r\n'
                                              '  runbookEngagementProcedureDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookEngagementProcedureListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementProcedureListDataV2 on '
                                              'RunbookEngagementProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  tenantId\r\n'
                                              '  clientId\r\n'
                                              '  engagementId\r\n'
                                              '  procedureId\r\n'
                                              '  description\r\n'
                                              '  outcomeRed\r\n'
                                              '  outcomeBlue\r\n'
                                              '  status\r\n'
                                              '  attackSource\r\n'
                                              '  notesRed\r\n'
                                              '  notesBlue\r\n'
                                              '  findingSeverity\r\n'
                                              '  runbookProcedure {\r\n'
                                              '    id\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_procedure_delete',
                             'name': 'RunbookEngagementProcedureDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns a list of RunbookV2 Engagements</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Engagements'],
                             'graphql_query': 'query RunbookEngagementListV2($args: ListArgs!) '
                                              '{\r\n'
                                              '    runbookEngagementListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookEngagementListDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementListDataV2 on '
                                              'RunbookEngagementV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  status\r\n'
                                              '  isCompleted\r\n'
                                              '  updatedAt\r\n'
                                              '  percentComplete\r\n'
                                              '  reportId\r\n'
                                              '  testPlan {\r\n'
                                              '    id\r\n'
                                              '    title\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  client {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_list',
                             'name': 'RunbookEngagementListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for an In Progess '
                                            'Engagement</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Engagements'],
                             'graphql_query': 'query RunbookEngagementDetailV2($engagementId: ID!) '
                                              '{\r\n'
                                              '  runbookEngagementV2(id: $engagementId) {\r\n'
                                              '    ...RunbookEngagementDetailV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementDetailV2 on '
                                              'RunbookEngagementV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  status\r\n'
                                              '  isCompleted\r\n'
                                              '  updatedAt\r\n'
                                              '  percentComplete\r\n'
                                              '  clientId\r\n'
                                              '  testPlan {\r\n'
                                              '    id\r\n'
                                              '    title\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  client {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_detail',
                             'name': 'RunbookEngagementDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Engagements'],
                             'graphql_query': 'mutation RunbookEngagementCreateV2($data: '
                                              'RunbookEngagementCreateInputV2!, $procedureIds: '
                                              '[ID!], $tags: [String!]) {\r\n'
                                              '  runbookEngagementCreateV2(\r\n'
                                              '    input: $data\r\n'
                                              '    procedureIds: $procedureIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementWizardFormV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementWizardFormV2 on '
                                              'RunbookEngagementV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  updatedAt\r\n'
                                              '  client {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  procedures {\r\n'
                                              '    ...RunbookEngagementWizardFormProcedureV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementWizardFormProcedureV2 on '
                                              'RunbookEngagementProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  runbookProcedure {\r\n'
                                              '    ...RunbookProcedureAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureAssignmentListDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookTechniqueAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueAssignmentListDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_create',
                             'name': 'RunbookEngagementCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Engagements'],
                             'graphql_query': 'mutation RunbookEngagementUpdateV2($id: ID!, $data: '
                                              'RunbookEngagementUpdateInputV2!, $procedureIds: '
                                              '[ID!], $tags: [String!]) {\r\n'
                                              '  runbookEngagementUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    input: $data\r\n'
                                              '    procedureIds: $procedureIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookEngagementWizardFormV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementWizardFormV2 on '
                                              'RunbookEngagementV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  updatedAt\r\n'
                                              '  client {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  procedures {\r\n'
                                              '    ...RunbookEngagementWizardFormProcedureV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementWizardFormProcedureV2 on '
                                              'RunbookEngagementProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  runbookProcedure {\r\n'
                                              '    ...RunbookProcedureAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureAssignmentListDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookTechniqueAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueAssignmentListDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_update',
                             'name': 'RunbookEngagementUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Engagements'],
                             'graphql_query': 'mutation RunbookEngagementDeleteV2($id: ID!) {\r\n'
                                              '  runbookEngagementDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookEngagementListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookEngagementListDataV2 on '
                                              'RunbookEngagementV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  status\r\n'
                                              '  isCompleted\r\n'
                                              '  updatedAt\r\n'
                                              '  percentComplete\r\n'
                                              '  reportId\r\n'
                                              '  testPlan {\r\n'
                                              '    id\r\n'
                                              '    title\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  client {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_delete',
                             'name': 'RunbookEngagementDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Submits a RunbookV2 Engagament and returns the ID '
                                            'of the created Report.</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Engagements'],
                             'graphql_query': 'mutation RunbookEngagementFinishV2($id: ID!) {\r\n'
                                              '  runbookEngagementFinishV2(id: $id)\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_engagement_finish',
                             'name': 'RunbookEngagementFinishV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns a list of RunbookV2 Test Plans</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Test Plans'],
                             'graphql_query': 'query RunbookTestPlanListV2($args: ListArgs!) {\r\n'
                                              '  runbookTestPlanListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookTestPlanListDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanListDataV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  procedureCount\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_test_plan_list',
                             'name': 'RunbookTestPlanListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for a RunbooksV2 Test Plan and '
                                            'all Procedures it contains</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Test Plans'],
                             'graphql_query': 'query RunbookTestPlanDetailV2($testPlanId: ID!) '
                                              '{\r\n'
                                              '  runbookTestPlanV2(id: $testPlanId) {\r\n'
                                              '    ...RunbookTestPlanDetailV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanDetailV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  procedures {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    description\r\n'
                                              '    shortName\r\n'
                                              '    isEditable\r\n'
                                              '    repository {\r\n'
                                              '      id\r\n'
                                              '      name\r\n'
                                              '      shortName\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    tags {\r\n'
                                              '      id\r\n'
                                              '      tag\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    techniques {\r\n'
                                              '      ...RunbookDetailTechniqueDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookDetailTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_test_plan_detail',
                             'name': 'RunbookTestPlanDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Test Plans'],
                             'graphql_query': 'mutation RunbookTestPlanCreateV2($data: '
                                              'RunbookTestPlanInputV2!, $procedureIds: [ID!], '
                                              '$tags: [String!]) {\r\n'
                                              '  runbookTestPlanCreateV2(input: $data, '
                                              'procedureIds: $procedureIds, tags: $tags) {\r\n'
                                              '    ...RunbookTestPlanWizardFormV2\r\n'
                                              '    ...RunbookTestPlanListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanWizardFormV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  procedures {\r\n'
                                              '    ...RunbookProcedureAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureAssignmentListDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookTechniqueAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueAssignmentListDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanListDataV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  procedureCount\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_test_plan_create',
                             'name': 'RunbookTestPlanCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Test Plans'],
                             'graphql_query': 'mutation RunbookTestPlanUpdateV2($id: ID!, $data: '
                                              'RunbookTestPlanInputV2!, $procedureIds: [ID!], '
                                              '$tags: [String!]) {\r\n'
                                              '  runbookTestPlanUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    input: $data\r\n'
                                              '    procedureIds: $procedureIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookTestPlanWizardFormV2\r\n'
                                              '    ...RunbookTestPlanListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanWizardFormV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  procedures {\r\n'
                                              '    ...RunbookProcedureAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureAssignmentListDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookTechniqueAssignmentListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueAssignmentListDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanListDataV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  procedureCount\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_test_plan_update',
                             'name': 'RunbookTestPlanUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'Test Plans'],
                             'graphql_query': 'mutation RunbookTestPlanDeleteV2($id: ID!) {\r\n'
                                              '  runbookTestPlanDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookTestPlanListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTestPlanListDataV2 on '
                                              'RunbookTestPlanV2 {\r\n'
                                              '  id\r\n'
                                              '  title\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  procedureCount\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_test_plan_delete',
                             'name': 'RunbookTestPlanDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories',
                                             'Users'],
                             'graphql_query': 'query RunbookRepositoryAvailableUserListV2($args: '
                                              'ListArgs!) {\r\n'
                                              '  runbookRepositoryAvailableUserListV2(args: $args) '
                                              '{\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookRepositoryAvailableUserData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      pagination {\r\n'
                                              '        total\r\n'
                                              '        __typename\r\n'
                                              '      }\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryAvailableUserData on '
                                              'RunbookRepositoryUserData {\r\n'
                                              '  id\r\n'
                                              '  user_id\r\n'
                                              '  fullName\r\n'
                                              '  email\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_available_user_list',
                             'name': 'RunbookRepositoryAvailableUserListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories',
                                             'Users'],
                             'graphql_query': 'query RunbookRepositoryUsersV2($repositoryId: ID!) '
                                              '{\r\n'
                                              '  runbookRepositoryUsersV2(id: $repositoryId) {\r\n'
                                              '    ...RunbookRepositoryUserV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryUserV2 on '
                                              'RunbookRepositoryUserV2 {\r\n'
                                              '  id\r\n'
                                              '  role\r\n'
                                              '  repositoryId\r\n'
                                              '  userId\r\n'
                                              '  userData {\r\n'
                                              '    id\r\n'
                                              '    user_id\r\n'
                                              '    fullName\r\n'
                                              '    email\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_users',
                             'name': 'RunbookRepositoryUsersV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories',
                                             'Users'],
                             'graphql_query': 'mutation RunbookRepositoryUsersAddV2($repositoryId: '
                                              'ID!, $users: '
                                              '[RunbookRepositoryUserCreateInputV2!]!) {\r\n'
                                              '  runbookRepositoryUsersAddV2(repositoryId: '
                                              '$repositoryId, users: $users) {\r\n'
                                              '    ...RunbookRepositoryUserV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryUserV2 on '
                                              'RunbookRepositoryUserV2 {\r\n'
                                              '  id\r\n'
                                              '  role\r\n'
                                              '  repositoryId\r\n'
                                              '  userId\r\n'
                                              '  userData {\r\n'
                                              '    id\r\n'
                                              '    user_id\r\n'
                                              '    fullName\r\n'
                                              '    email\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_users_add',
                             'name': 'RunbookRepositoryUsersAddV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Can update the permission of a user in the '
                                            'RunbookDB Repository.</p>\n'
                                            '<p><code>role</code> can be one of <code>["viewer", '
                                            '"editor"]</code></p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories',
                                             'Users'],
                             'graphql_query': 'mutation '
                                              'RunbookRepositoryUserUpdateV2($repositoryId: ID!, '
                                              '$userId: ID!, $data: '
                                              'RunbookRepositoryUserUpdateInputV2!) {\r\n'
                                              '  runbookRepositoryUserUpdateV2(\r\n'
                                              '    repositoryId: $repositoryId\r\n'
                                              '    userId: $userId\r\n'
                                              '    input: $data\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookRepositoryUserV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryUserV2 on '
                                              'RunbookRepositoryUserV2 {\r\n'
                                              '  id\r\n'
                                              '  role\r\n'
                                              '  repositoryId\r\n'
                                              '  userId\r\n'
                                              '  userData {\r\n'
                                              '    id\r\n'
                                              '    user_id\r\n'
                                              '    fullName\r\n'
                                              '    email\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_user_update',
                             'name': 'RunbookRepositoryUserUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories',
                                             'Users'],
                             'graphql_query': 'mutation '
                                              'RunbookRepositoryUserRemoveV2($repositoryId: ID!, '
                                              '$userId: ID!) {\r\n'
                                              '  runbookRepositoryUserRemoveV2(repositoryId: '
                                              '$repositoryId, userId: $userId) {\r\n'
                                              '    ...RunbookRepositoryUserV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryUserV2 on '
                                              'RunbookRepositoryUserV2 {\r\n'
                                              '  id\r\n'
                                              '  role\r\n'
                                              '  repositoryId\r\n'
                                              '  userId\r\n'
                                              '  userData {\r\n'
                                              '    id\r\n'
                                              '    user_id\r\n'
                                              '    fullName\r\n'
                                              '    email\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_user_remove',
                             'name': 'RunbookRepositoryUserRemoveV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns a list of all Repositories in the '
                                            'RunbooksDB</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories'],
                             'graphql_query': 'query RunbookRepositoryListV2($args: ListArgs!) '
                                              '{\r\n'
                                              '  runbookRepositoryListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookRepositoryListDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryListDataV2 on '
                                              'RunbookRepositoryV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  procedures {\r\n'
                                              '    id\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  userCount\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_list',
                             'name': 'RunbookRepositoryListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for a RunbooksV2 Repository and a '
                                            'list of Procedures it contains</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories'],
                             'graphql_query': 'query RunbookRepositoryDetailV2($repositoryId: ID!, '
                                              '$procedureListArgs: ListArgs!) {\r\n'
                                              '  runbookRepositoryV2(id: $repositoryId) {\r\n'
                                              '    ...RunbookRepositoryDetailV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  runbookProcedureListV2(args: $procedureListArgs) '
                                              '{\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookProcedureDataGridV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryDetailV2 on '
                                              'RunbookRepositoryV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureDataGridV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  repository {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    type\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    methodologies {\r\n'
                                              '      name\r\n'
                                              '      shortName\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_detail',
                             'name': 'RunbookRepositoryDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Create a RunbookDB Repository.</p>\n'
                                            '<p>Must have a unique <code>shortName</code> '
                                            '(<code>Repository ID Prefix</code> in platform)</p>\n'
                                            '<p><code>type</code> can be one of <code>["private", '
                                            '"managed", "open"]</code></p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories'],
                             'graphql_query': 'mutation RunbookRepositoryCreateV2($data: '
                                              'RunbookRepositoryInputV2!) {\r\n'
                                              '  runbookRepositoryCreateV2(input: $data) {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    description\r\n'
                                              '    type\r\n'
                                              '    isEditable\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_create',
                             'name': 'RunbookRepositoryCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories'],
                             'graphql_query': 'mutation RunbookRepositoryUpdateV2($data: '
                                              'RunbookRepositoryInputV2!, $repositoryId: ID!) {\r\n'
                                              '  runbookRepositoryUpdateV2(input: $data, id: '
                                              '$repositoryId) {\r\n'
                                              '    ...RunbookRepositoryUpdateDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookRepositoryUpdateDataV2 on '
                                              'RunbookRepositoryV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  type\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_update',
                             'name': 'RunbookRepositoryUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Repositories'],
                             'graphql_query': 'mutation RunbookRepositoryDeleteV2($id: ID!) {\r\n'
                                              '  runbookRepositoryDeleteV2(id: $id) {\r\n'
                                              '    id\r\n'
                                              '    deletedAt\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_repository_delete',
                             'name': 'RunbookRepositoryDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns a list of Methodologies in the '
                                            'RunbooksDB</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Methodologies'],
                             'graphql_query': 'query RunbookMethodologyListV2($args: ListArgs!) '
                                              '{\r\n'
                                              '  runbookMethodologyListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookMethodologyListDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyListDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  isEditable\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_methodology_list',
                             'name': 'RunbookMethodologyListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for a RunbooksV2 '
                                            'Methodology</p>\n',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Methodologies'],
                             'graphql_query': 'query RunbookMethodologyDetailV2($methodologyId: '
                                              'ID!) {\r\n'
                                              '  runbookMethodologyV2(id: $methodologyId) {\r\n'
                                              '    ...RunbookMethodologyFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyFormDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  tactics {\r\n'
                                              '    ...RunbookMethodologyFormTacticDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyFormTacticDataV2 on '
                                              'RunbookTacticV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_methodology_detail',
                             'name': 'RunbookMethodologyDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Methodologies'],
                             'graphql_query': 'mutation RunbookMethodologyCreateV2($data: '
                                              'RunbookMethodologyInputV2!, $tacticIds: [ID!], '
                                              '$tags: [String!]) {\r\n'
                                              '  runbookMethodologyCreateV2(input: $data, '
                                              'tacticIds: $tacticIds, tags: $tags) {\r\n'
                                              '    ...RunbookMethodologyFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyFormDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  tactics {\r\n'
                                              '    ...RunbookMethodologyFormTacticDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyFormTacticDataV2 on '
                                              'RunbookTacticV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_methodology_create',
                             'name': 'RunbookMethodologyCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Methodologies'],
                             'graphql_query': 'mutation RunbookMethodologyUpdateV2($id: ID!, '
                                              '$data: RunbookMethodologyInputV2!, $tacticIds: '
                                              '[ID!], $tags: [String!]) {\r\n'
                                              '  runbookMethodologyUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    input: $data\r\n'
                                              '    tacticIds: $tacticIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookMethodologyFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyFormDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  tactics {\r\n'
                                              '    ...RunbookMethodologyFormTacticDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyFormTacticDataV2 on '
                                              'RunbookTacticV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_methodology_update',
                             'name': 'RunbookMethodologyUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks',
                                             'Runbooks v2',
                                             'RunbooksDB',
                                             'Methodologies'],
                             'graphql_query': 'mutation RunbookMethodologyDeleteV2($id: ID!) {\r\n'
                                              '  runbookMethodologyDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookMethodologyListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookMethodologyListDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  isEditable\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_methodology_delete',
                             'name': 'RunbookMethodologyDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns a list of Tactics in the RunbooksDB</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Tactics'],
                             'graphql_query': 'query RunbookTacticListV2($args: ListArgs!) {\r\n'
                                              '  runbookTacticListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookTacticListDataV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticListDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  isEditable\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_tactic_list',
                             'name': 'RunbookTacticListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for a RunbooksV2 Tactic</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Tactics'],
                             'graphql_query': 'query RunbookTacticDetailV2($tacticId: ID!) {\r\n'
                                              '  runbookTacticV2(id: $tacticId) {\r\n'
                                              '    ...RunbookTacticFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    ...RunbookTacticFormMethodologyDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormMethodologyDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_tactic_detail',
                             'name': 'RunbookTacticDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Tactics'],
                             'graphql_query': 'mutation RunbookTacticCreateV2($data: '
                                              'RunbookTacticInputV2!, $methodologyIds: [ID!], '
                                              '$techniqueIds: [ID!], $tags: [String!]) {\r\n'
                                              '  runbookTacticCreateV2(\r\n'
                                              '    input: $data\r\n'
                                              '    methodologyIds: $methodologyIds\r\n'
                                              '    techniqueIds: $techniqueIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookTacticFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    ...RunbookTacticFormMethodologyDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormMethodologyDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_tactic_create',
                             'name': 'RunbookTacticCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Tactics'],
                             'graphql_query': 'mutation RunbookTacticUpdateV2($id: ID!, $data: '
                                              'RunbookTacticInputV2!, $methodologyIds: [ID!], '
                                              '$techniqueIds: [ID!], $tags: [String!]) {\r\n'
                                              '  runbookTacticUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    input: $data\r\n'
                                              '    methodologyIds: $methodologyIds\r\n'
                                              '    techniqueIds: $techniqueIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookTacticFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    ...RunbookTacticFormMethodologyDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormMethodologyDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_tactic_update',
                             'name': 'RunbookTacticUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Tactics'],
                             'graphql_query': 'mutation RunbookTacticDeleteV2($id: ID!) {\r\n'
                                              '  runbookTacticDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookTacticListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticListDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  isEditable\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_tactic_delete',
                             'name': 'RunbookTacticDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>StartFragment</p>\n'
                                            '<p>Returns a list of Techniques in the '
                                            'RunbooksDB</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Techniques'],
                             'graphql_query': 'query RunbookTechniqueListV2($args: ListArgs!) {\r\n'
                                              '  runbookTechniqueListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookTechniqueDataGridV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueDataGridV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_technique_list',
                             'name': 'RunbookTechniqueListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for a RunbooksV2 Technique</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Techniques'],
                             'graphql_query': 'query RunbookTechniqueDetailV2($techniqueId: ID!) '
                                              '{\r\n'
                                              '  runbookTechniqueV2(id: $techniqueId) {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    description\r\n'
                                              '    procedures {\r\n'
                                              '      id\r\n'
                                              '      name\r\n'
                                              '      shortName\r\n'
                                              '      techniques {\r\n'
                                              '        ...RunbookProcedureDetailTechniqueV2\r\n'
                                              '        __typename\r\n'
                                              '      }\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    tactics {\r\n'
                                              '      ...RunbookTacticDetailV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    tags {\r\n'
                                              '      id\r\n'
                                              '      tag\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureDetailTechniqueV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    methodologies {\r\n'
                                              '      id\r\n'
                                              '      name\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticDetailV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  ...RunbookTacticFormDataV2\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  methodologies {\r\n'
                                              '    ...RunbookTacticFormMethodologyDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticFormMethodologyDataV2 on '
                                              'RunbookMethodologyV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_technique_detail',
                             'name': 'RunbookTechniqueDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Techniques'],
                             'graphql_query': 'mutation RunbookTechniqueCreateV2($data: '
                                              'RunbookTechniqueInputV2!, $tacticIds: [ID!], '
                                              '$procedureIds: [ID!], $tags: [String!]) {\r\n'
                                              '  runbookTechniqueCreateV2(\r\n'
                                              '    input: $data\r\n'
                                              '    tacticIds: $tacticIds\r\n'
                                              '    procedureIds: $procedureIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookTechniqueFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueFormDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  procedures {\r\n'
                                              '    ...RunbookProcedureFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    ...RunbookTacticListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  repositoryId\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  executionSteps {\r\n'
                                              '    id\r\n'
                                              '    description\r\n'
                                              '    successCriteria\r\n'
                                              '    sortOrder\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticListDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  isEditable\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_technique_create',
                             'name': 'RunbookTechniqueCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Techniques'],
                             'graphql_query': 'mutation RunbookTechniqueUpdateV2($data: '
                                              'RunbookTechniqueInputV2!, $id: ID!, $tacticIds: '
                                              '[ID!], $procedureIds: [ID!], $tags: [String!]) {\r\n'
                                              '  runbookTechniqueUpdateV2(\r\n'
                                              '    input: $data\r\n'
                                              '    id: $id\r\n'
                                              '    tacticIds: $tacticIds\r\n'
                                              '    procedureIds: $procedureIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookTechniqueFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueFormDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  procedures {\r\n'
                                              '    ...RunbookProcedureFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tactics {\r\n'
                                              '    ...RunbookTacticListDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  repositoryId\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  executionSteps {\r\n'
                                              '    id\r\n'
                                              '    description\r\n'
                                              '    successCriteria\r\n'
                                              '    sortOrder\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTacticListDataV2 on RunbookTacticV2 '
                                              '{\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  isEditable\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_technique_update',
                             'name': 'RunbookTechniqueUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Techniques'],
                             'graphql_query': 'mutation RunbookTechniqueDeleteV2($id: ID!) {\r\n'
                                              '  runbookTechniqueDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookTechniqueDataGridV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookTechniqueDataGridV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_technique_delete',
                             'name': 'RunbookTechniqueDeleteV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns a list of Procedures in the '
                                            'RunbooksDB</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Procedures'],
                             'graphql_query': 'query RunbookProcedureListV2($args: ListArgs!) {\r\n'
                                              '  runbookProcedureListV2(args: $args) {\r\n'
                                              '    data {\r\n'
                                              '      ...RunbookProcedureDataGridV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    meta {\r\n'
                                              '      ...ListMetaData\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureDataGridV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  repository {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    type\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    methodologies {\r\n'
                                              '      name\r\n'
                                              '      shortName\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment ListMetaData on ListMeta {\r\n'
                                              '  pagination {\r\n'
                                              '    limit\r\n'
                                              '    offset\r\n'
                                              '    total\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  sort {\r\n'
                                              '    by\r\n'
                                              '    order\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  filters {\r\n'
                                              '    by\r\n'
                                              '    value\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_procedure_list',
                             'name': 'RunbookProcedureListV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '<p>Returns the data for a RunbooksV2 Procedure</p>\n',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Procedures'],
                             'graphql_query': 'query RunbookProcedureDetailV2($id: ID!) {\r\n'
                                              '  runbookProcedureV2(id: $id) {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    description\r\n'
                                              '    shortName\r\n'
                                              '    isEditable\r\n'
                                              '    repository {\r\n'
                                              '      id\r\n'
                                              '      name\r\n'
                                              '      shortName\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    tags {\r\n'
                                              '      id\r\n'
                                              '      tag\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    executionSteps {\r\n'
                                              '      id\r\n'
                                              '      description\r\n'
                                              '      successCriteria\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    techniques {\r\n'
                                              '      ...RunbookProcedureDetailTechniqueV2\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureDetailTechniqueV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    methodologies {\r\n'
                                              '      id\r\n'
                                              '      name\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_procedure_detail',
                             'name': 'RunbookProcedureDetailV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Procedures'],
                             'graphql_query': 'mutation RunbookProcedureCreateV2($data: '
                                              'RunbookProcedureInputV2!, $executionSteps: '
                                              '[RunbookProcedureExecutionStepInput!]!, '
                                              '$techniqueIds: [ID!], $tags: [String!]) {\r\n'
                                              '  runbookProcedureCreateV2(\r\n'
                                              '    input: $data\r\n'
                                              '    executionSteps: $executionSteps\r\n'
                                              '    techniqueIds: $techniqueIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookProcedureFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  repositoryId\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  executionSteps {\r\n'
                                              '    id\r\n'
                                              '    description\r\n'
                                              '    successCriteria\r\n'
                                              '    sortOrder\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_procedure_create',
                             'name': 'RunbookProcedureCreateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Procedures'],
                             'graphql_query': 'mutation RunbookProcedureUpdateV2($id: ID!, $data: '
                                              'RunbookProcedureInputV2!, $executionSteps: '
                                              '[RunbookProcedureExecutionStepInput!]!, '
                                              '$techniqueIds: [ID!], $tags: [String!]) {\r\n'
                                              '  runbookProcedureUpdateV2(\r\n'
                                              '    id: $id\r\n'
                                              '    input: $data\r\n'
                                              '    executionSteps: $executionSteps\r\n'
                                              '    techniqueIds: $techniqueIds\r\n'
                                              '    tags: $tags\r\n'
                                              '  ) {\r\n'
                                              '    ...RunbookProcedureFormDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormDataV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  repositoryId\r\n'
                                              '  tags {\r\n'
                                              '    id\r\n'
                                              '    tag\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  executionSteps {\r\n'
                                              '    id\r\n'
                                              '    description\r\n'
                                              '    successCriteria\r\n'
                                              '    sortOrder\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    ...RunbookProcedureFormTechniqueDataV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureFormTechniqueDataV2 on '
                                              'RunbookTechniqueV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  tactics {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  methodologies {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_procedure_update',
                             'name': 'RunbookProcedureUpdateV2',
                             'path': '/graphql'},
                            {'aliases': [],
                             'body_mode': 'graphql',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks', 'Runbooks v2', 'RunbooksDB', 'Procedures'],
                             'graphql_query': 'mutation RunbookProcedureDeleteV2($id: ID!) {\r\n'
                                              '  runbookProcedureDeleteV2(id: $id) {\r\n'
                                              '    ...RunbookProcedureDataGridV2\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '}\r\n'
                                              '\r\n'
                                              'fragment RunbookProcedureDataGridV2 on '
                                              'RunbookProcedureV2 {\r\n'
                                              '  id\r\n'
                                              '  name\r\n'
                                              '  shortName\r\n'
                                              '  description\r\n'
                                              '  isEditable\r\n'
                                              '  updatedAt\r\n'
                                              '  deletedAt\r\n'
                                              '  repository {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    type\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  techniques {\r\n'
                                              '    id\r\n'
                                              '    name\r\n'
                                              '    shortName\r\n'
                                              '    methodologies {\r\n'
                                              '      name\r\n'
                                              '      shortName\r\n'
                                              '      __typename\r\n'
                                              '    }\r\n'
                                              '    __typename\r\n'
                                              '  }\r\n'
                                              '  __typename\r\n'
                                              '}',
                             'method': 'POST',
                             'method_name': 'runbook_procedure_delete',
                             'name': 'RunbookProcedureDeleteV2',
                             'path': '/graphql'},
                            {'aliases': ['export'],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks'],
                             'graphql_query': None,
                             'method': 'GET',
                             'method_name': 'export_runbook',
                             'name': 'Export Runbook',
                             'path': '/api/v1/export/runbook/{runbookId}'},
                            {'aliases': [],
                             'body_mode': 'none',
                             'default_params': [],
                             'description': '',
                             'folder_path': ['Runbooks'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'import_runbook',
                             'name': 'Import Runbook',
                             'path': '/api/v1/import/runbook'}]},
 'scheduler': {'display_name': 'Scheduler',
               'endpoints': [{'aliases': [],
                              'body_mode': 'formdata',
                              'default_params': [],
                              'description': '<p>Upload a file artifact to an existing Engagement '
                                             'Schedule Event.</p>\n',
                              'folder_path': ['Scheduler', 'Artifacts'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'create_engagement_schedule_event_artifact',
                              'name': 'Create Engagement Schedule Event Artifact',
                              'path': '/api/v2/engagement-schedule-artifacts'},
                             {'aliases': [],
                              'body_mode': 'formdata',
                              'default_params': [('clientCuid', '{clientCUID}')],
                              'description': '<p>Get information about an existing file artifact '
                                             'on an Engagement Schedule Event.</p>\n',
                              'folder_path': ['Scheduler', 'Artifacts'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'get_engagement_schedule_event_artifacts',
                              'name': 'Get Engagement Schedule Event Artifacts',
                              'path': '/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>Updates a file artifact on an Engagement Schedule '
                                             'Event.</p>\n'
                                             '<p>The only updatable properties are '
                                             '<code>clientCuid</code> and '
                                             '<code>engagementScheduleEventCuid</code>. This means '
                                             'this endpoint is less about updating the file '
                                             'artifact, but rather updating which Engagement '
                                             'Schedule Event the file artifact is associated '
                                             'with.</p>\n',
                              'folder_path': ['Scheduler', 'Artifacts'],
                              'graphql_query': None,
                              'method': 'PATCH',
                              'method_name': 'update_engagement_schedule_event_artifact',
                              'name': 'Update Engagement Schedule Event Artifact',
                              'path': '/api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [('clientCuid', '{clientCUID}')],
                              'description': '<p>Deletes a file artifact and removes its '
                                             'association with an Engagement Schedule Event.</p>\n',
                              'folder_path': ['Scheduler', 'Artifacts'],
                              'graphql_query': None,
                              'method': 'DELETE',
                              'method_name': 'delete_engagement_schedule_event_artifact',
                              'name': 'Delete Engagement Schedule Event Artifact',
                              'path': '/api/v2/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [('clientCuid', '{clientCUID}')],
                              'description': '',
                              'folder_path': ['Scheduler', 'Artifacts'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'download_engagement_schedule_event_artifact',
                              'name': 'Download Engagement Schedule Event Artifact',
                              'path': '/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/engagement-schedule-artifacts/{engagementScheduleArtifactCuid}'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>Get paginated multiple Engagement Schedule Events '
                                             'based on a filter.</p>\n',
                              'folder_path': ['Scheduler'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'find_many_engagement_schedule_events',
                              'name': 'Find Many Engagement Schedule Events',
                              'path': '/api/v2/engagement-schedule-events/search'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>Get an existing Engagement Schedule Event '
                                             'object.</p>\n',
                              'folder_path': ['Scheduler'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'get_engagement_schedule_event_by_id',
                              'name': 'Get Engagement Schedule Event by ID',
                              'path': '/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>Used to create a new Engagement Schedule '
                                             'Event.</p>\n'
                                             '<p><strong>Important:</strong> There are 2 endpoints '
                                             'needed to create events. In the UI there are '
                                             'multiple confirmation screens to create the new '
                                             'Engagement. This endpoint covers the first screen, '
                                             '<strong>Enter engagement details</strong>. The '
                                             'screens <strong>Enter report details</strong>, and '
                                             '<strong>Select dates &amp; assign operators</strong> '
                                             'are covered by <a '
                                             'href="https://api-docs.plextrac.com/#f33eae9b-6026-4e8e-8723-a20e63250704">POST '
                                             'Approve Engagement Schedule Event</a> '
                                             'endpoint.</p>\n',
                              'folder_path': ['Scheduler'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'create_engagement_schedule_event',
                              'name': 'Create Engagement Schedule Event',
                              'path': '/api/v2/engagement-schedule-events'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>Endpoint used in the process to create a new '
                                             'Engagement, or update an existing Engagement.</p>\n',
                              'folder_path': ['Scheduler'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'approve_engagement_schedule_event',
                              'name': 'Approve Engagement Schedule Event',
                              'path': '/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}/approve'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>Update any information on the scheduleEvent '
                                             'object. To update the <code>assignedOperators</code> '
                                             'or <code>report</code>, use <a '
                                             'href="https://api-docs.plextrac.com/#f33eae9b-6026-4e8e-8723-a20e63250704">POST '
                                             'Approve Engagement Schedule Event</a>.</p>\n'
                                             '<p><strong>NOTE:</strong> Engagement Schedule Events '
                                             'cannot be deleted. This endpoint can be used to set '
                                             'the event to <code>CANCELED</code>, effective '
                                             'deleting the event.</p>\n',
                              'folder_path': ['Scheduler'],
                              'graphql_query': None,
                              'method': 'PATCH',
                              'method_name': 'update_engagement_schedule_event',
                              'name': 'Update Engagement Schedule Event',
                              'path': '/api/v2/engagement-schedule-events/{engagementScheduleEventCuid}'}]},
 'substatus': {'display_name': 'Substatus',
               'endpoints': [{'aliases': ['list'],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Substatus'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'list_substatus',
                              'name': 'List Substatus',
                              'path': '/api/v3/substatus'},
                             {'aliases': ['create'],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Substatus'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'create_substatus',
                              'name': 'Create Substatus',
                              'path': '/api/v3/substatus'},
                             {'aliases': ['update'],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Substatus'],
                              'graphql_query': None,
                              'method': 'PATCH',
                              'method_name': 'update_substatus',
                              'name': 'Update Substatus',
                              'path': '/api/v3/substatus/{substatusCuid}'},
                             {'aliases': ['delete'],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Substatus'],
                              'graphql_query': None,
                              'method': 'DELETE',
                              'method_name': 'delete_substatus',
                              'name': 'Delete Substatus',
                              'path': '/api/v3/substatus/{substatusCuid}'}]},
 'templates': {'display_name': 'Templates',
               'endpoints': [{'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>This request <strong>lists all report '
                                             'templates</strong> for a tenant.</p>\n',
                              'folder_path': ['Templates', 'Report Templates'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'list_report_templates',
                              'name': 'List Report Templates',
                              'path': '/api/v1/tenant/{tenantId}/report-templates'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>This request <strong>retrieves a specific report '
                                             'template</strong> within a tenant.</p>\n'
                                             '<p>Please see our public docs for more information '
                                             'about how <a '
                                             'href="https://docs.plextrac.com/plextrac-documentation/product-documentation-1/account-management/account-admin/customizations/templates/report-templates">Report '
                                             'Templates</a> fit into the process of exporting a '
                                             'report.</p>\n',
                              'folder_path': ['Templates', 'Report Templates'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'get_report_template',
                              'name': 'Get Report Template',
                              'path': '/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>This request <strong>creates</strong> <strong>a '
                                             'report template</strong> within a tenant.</p>\n',
                              'folder_path': ['Templates', 'Report Templates'],
                              'graphql_query': None,
                              'method': 'PUT',
                              'method_name': 'create_report_template',
                              'name': 'Create Report Template',
                              'path': '/api/v1/tenant/{tenantId}/report-template'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>This request <strong>updates</strong> <strong>a '
                                             'report template</strong> within a tenant.</p>\n',
                              'folder_path': ['Templates', 'Report Templates'],
                              'graphql_query': None,
                              'method': 'PUT',
                              'method_name': 'update_report_template',
                              'name': 'Update Report Template',
                              'path': '/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Templates', 'Report Templates'],
                              'graphql_query': None,
                              'method': 'DELETE',
                              'method_name': 'delete_report_template',
                              'name': 'Delete Report Template',
                              'path': '/api/v1/tenant/{tenantId}/report-template/{reportTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>This request <strong>lists all findings '
                                             'templates</strong> for a tenant.</p>\n',
                              'folder_path': ['Templates', 'Findings Templates/Layouts'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'list_findings_templates',
                              'name': 'List Findings Templates',
                              'path': '/api/v1/field-templates'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>This request retrieves <strong>a findings '
                                             'template</strong></p>\n',
                              'folder_path': ['Templates', 'Findings Templates/Layouts'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'get_findings_template',
                              'name': 'Get Findings Template',
                              'path': '/api/v1/field-template/{findingTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>This request <strong>creates</strong> <strong>a '
                                             'findings template</strong> within a tenant.</p>\n',
                              'folder_path': ['Templates', 'Findings Templates/Layouts'],
                              'graphql_query': None,
                              'method': 'PUT',
                              'method_name': 'create_finding_template',
                              'name': 'Create Finding Template',
                              'path': '/api/v1/tenant/{tenantId}/field-template'},
                             {'aliases': [],
                              'body_mode': 'raw',
                              'default_params': [],
                              'description': '<p>Update a finding template in your tenancy</p>\n',
                              'folder_path': ['Templates', 'Findings Templates/Layouts'],
                              'graphql_query': None,
                              'method': 'PUT',
                              'method_name': 'update_finding_template',
                              'name': 'Update Finding Template',
                              'path': '/api/v1/tenant/{tenantId}/field-template/{findingTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Templates', 'Findings Templates/Layouts'],
                              'graphql_query': None,
                              'method': 'DELETE',
                              'method_name': 'delete_finding_template',
                              'name': 'Delete Finding Template',
                              'path': '/api/v1/tenant/{tenantId}/field-template/{findingTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>Returns a list of all Export Templates in the '
                                             'tenant.</p>\n'
                                             '<p>Please see our public docs for more information '
                                             'about how <a '
                                             'href="https://docs.plextrac.com/plextrac-documentation/product-documentation-1/account-management/account-admin/customizations/templates/export-templates">Export '
                                             'Templates</a> fit into the process of exporting a '
                                             'report.</p>\n',
                              'folder_path': ['Templates', 'Export Templates'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'list_export_templates',
                              'name': 'List Export Templates',
                              'path': '/api/v2/tenant/{tenantId}/export-templates'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '<p>Returns the file binary of the .docx file of the '
                                             'Export Template.</p>\n',
                              'folder_path': ['Templates', 'Export Templates'],
                              'graphql_query': None,
                              'method': 'GET',
                              'method_name': 'get_export_template',
                              'name': 'Get Export Template',
                              'path': '/api/v1/tenant/{tenantId}/export-template/{exportTemplateId}'},
                             {'aliases': [],
                              'body_mode': 'formdata',
                              'default_params': [('name', 'plextrac-default-template.docx'),
                                                 ('type', 'custom')],
                              'description': '<p>Imports a file with Jinja code into the platform '
                                             'as an export template. You can add files for either '
                                             'a Word (.docx) or PDF (.j2) template. Files must be '
                                             'uploaded from you file system and have one of the '
                                             'proper file extensions.</p>\n'
                                             '<p><strong>Notes:</strong></p>\n'
                                             '<ul>\n'
                                             '<li><p>The query param <code>name</code> must be the '
                                             'exact name of the file in your file system, '
                                             'including extension.</p>\n'
                                             '</li>\n'
                                             '<li><p>Regardless of file type, the query param '
                                             '<code>type</code> should always be '
                                             '<code>custom</code>.</p>\n'
                                             '</li>\n'
                                             '</ul>\n',
                              'folder_path': ['Templates', 'Export Templates'],
                              'graphql_query': None,
                              'method': 'POST',
                              'method_name': 'import_export_template',
                              'name': 'Import Export Template',
                              'path': '/api/v1/tenant/{tenantId}/template/import'},
                             {'aliases': [],
                              'body_mode': 'none',
                              'default_params': [],
                              'description': '',
                              'folder_path': ['Templates', 'Export Templates'],
                              'graphql_query': None,
                              'method': 'DELETE',
                              'method_name': 'delete_export_template',
                              'name': 'Delete Export Template',
                              'path': '/api/v1/tenant/{tenantId}/template/{exportTemplateId}'}]},
 'tenant': {'display_name': 'Tenant',
            'endpoints': [{'aliases': [],
                           'body_mode': 'raw',
                           'default_params': [],
                           'description': '',
                           'folder_path': ['Tenant', 'Settings'],
                           'graphql_query': None,
                           'method': 'PUT',
                           'method_name': 'update_settings',
                           'name': 'Update settings',
                           'path': '/api/v2/tenants/{tenantId}/settings'},
                          {'aliases': ['get'],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>This request <strong>obtains information about a '
                                          'tenant</strong>, such as ID, settings, point of contact '
                                          'information, etc.</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'get_tenant',
                           'name': 'Get Tenant',
                           'path': '/api/v1/tenant/{tenantId}'},
                          {'aliases': ['update'],
                           'body_mode': 'none',
                           'default_params': [('name', 'Me!')],
                           'description': '<p>Update the details of your tenant, including '
                                          '<code>name</code>, <code>address</code>, and '
                                          '<code>point of contact</code></p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'PUT',
                           'method_name': 'update_tenant',
                           'name': 'Update Tenant',
                           'path': '/api/v1/tenant/{tenantId}'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>This request <strong>retrieves the number of days to '
                                          'wait</strong> before reminding users to provide status '
                                          'updates on assigned findings.</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'get_notification_settings',
                           'name': 'Get Notification Settings',
                           'path': '/api/v1/tenant/{tenantId}/notificationsettings'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [('reminderDays', 'number')],
                           'description': '<p>Update the number of days to wait before reminding '
                                          'users to provide status updates on findings assigned to '
                                          'them</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'PUT',
                           'method_name': 'update_notification_settings',
                           'name': 'Update Notification Settings',
                           'path': '/api/v1/tenant/{tenantId}/notificationsettings'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>This request retrieves <strong>analytics for a '
                                          'tenant,</strong> providing a total count of findings by '
                                          'risk and status.</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'tenant_analytics',
                           'name': 'Tenant Analytics',
                           'path': '/api/v1/tenant/{tenantId}/analytics'},
                          {'aliases': [],
                           'body_mode': 'formdata',
                           'default_params': [],
                           'description': '<p>Add a logo for your tenancy</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'POST',
                           'method_name': 'add_tenant_logo',
                           'name': 'Add Tenant Logo',
                           'path': '/api/v1/tenant/{tenantId}/logo'},
                          {'aliases': [],
                           'body_mode': 'formdata',
                           'default_params': [],
                           'description': '<p>Add a logo for your tenancy</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'POST',
                           'method_name': 'add_tenant_logo_dark',
                           'name': 'Add Tenant Logo Dark',
                           'path': '/api/v1/tenant/{tenantId}/logo/dark'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>Remove the logo from your tenancy. This action will '
                                          'result in the PlexTrac logo being displayed.</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'DELETE',
                           'method_name': 'delete_tenant_logo',
                           'name': 'Delete Tenant Logo',
                           'path': '/api/v1/tenant/{tenantId}/logo'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>Remove the logo from your tenancy. This action will '
                                          'result in the PlexTrac logo being displayed.</p>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'DELETE',
                           'method_name': 'delete_tenant_logo_dark',
                           'name': 'Delete Tenant Logo Dark',
                           'path': '/api/v1/tenant/{tenantId}/logo/dark'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'DELETE',
                           'method_name': 'delete_tenant_icon',
                           'name': 'Delete Tenant Icon',
                           'path': '/api/v1/tenant/{tenantId}/icon'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'DELETE',
                           'method_name': 'delete_tenant_icon_dark',
                           'name': 'Delete Tenant Icon Dark',
                           'path': '/api/v1/tenant/{tenantId}/icon/dark'},
                          {'aliases': [],
                           'body_mode': 'none',
                           'default_params': [],
                           'description': '<p>Root request. You can determine that the instance is '
                                          'up and running if this request returns the following '
                                          'JSON</p>\n'
                                          '<pre class="click-to-expand-wrapper '
                                          'is-snippet-wrapper"><code class="language-json">{\n'
                                          '    "text": "Authenticate at /authenticate"\n'
                                          '}\n'
                                          '\n'
                                          '</code></pre>\n',
                           'folder_path': ['Tenant'],
                           'graphql_query': None,
                           'method': 'GET',
                           'method_name': 'root_request',
                           'name': 'Root Request',
                           'path': '/api/v1/'}]},
 'users': {'display_name': 'Users',
           'endpoints': [{'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request <strong>retrieves user info</strong> '
                                         'about the currently authenticated user.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_authenticated_user',
                          'name': 'Get Authenticated User v2',
                          'path': '/api/v2/whoami'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request <strong>retrieves a list of all '
                                         'users</strong> in a tenant.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'list_tenant_users',
                          'name': 'List Tenant Users',
                          'path': '/api/v1/tenant/{tenantId}/user/list'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [('offset', '0'),
                                             ('limit', '10'),
                                             ('sortBy', 'firstName'),
                                             ('order', 'DESEND'),
                                             ('filter', '')],
                          'description': '<p>This request <strong>retrieves a paginated list of '
                                         'all users</strong> in a tenant.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_tenants_users',
                          'name': 'Get Tenants Users',
                          'path': '/api/v2/tenants/{tenantId}/users'},
                         {'aliases': [],
                          'body_mode': 'formdata',
                          'default_params': [],
                          'description': '<p>Create a new user in your tenant</p>\n'
                                         '<p><strong>This route is deprecated and will be blocked '
                                         'in a future release, please now '
                                         'call:{domain}/tenant/{tenantId}/user/create/bulk</strong></p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'create_user_deprecated',
                          'name': 'Create User (DEPRECATED)',
                          'path': '/api/v1/tenant/{tenantId}/user/create'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Create new users in your tenant.</p>\n'
                                         '<p><code>role</code> can be one of the defaults "ADMIN", '
                                         '"STD_USER", or "ANALYST". For custom RBAC roles you need '
                                         'to find the <code>key</code> for your custom role. Then '
                                         'the use the pattern TENANT_[tenant ID]_ROLE_[key of '
                                         'custom RBAC role] e.g. '
                                         '"TENANT_0_ROLE_MY_CUSTOM_ROLE"</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'bulk_create_user',
                          'name': 'Bulk Create User',
                          'path': '/api/v1/tenant/{tenantId}/user/create/bulk'},
                         {'aliases': ['update'],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request <strong>updates information</strong> '
                                         'about the user executing the endpoint.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'update_user',
                          'name': 'Update User',
                          'path': '/api/v1/user/update'},
                         {'aliases': ['delete'],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request <strong>deletes</strong> the user '
                                         'associated with the email sent in the payload.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'DELETE',
                          'method_name': 'delete_user',
                          'name': 'Delete User',
                          'path': '/api/v2/user/delete'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request <strong>changes the password</strong> '
                                         'for the user making the request. You cannot change '
                                         'another users password.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'change_password',
                          'name': 'Change Password',
                          'path': '/api/v1/user/changepass'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request <strong>sends a password recovery '
                                         'email</strong> to an existing user based on the email '
                                         'address provided in the query.</p>\n'
                                         "<p>This endpoint doesn't require authenication.</p>\n",
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'forgot_password',
                          'name': 'Forgot Password',
                          'path': '/api/v1/user/forgotpass'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Send an email for a user to reset their '
                                         'password.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'reset_user_password',
                          'name': 'Reset User Password',
                          'path': '/api/v1/tenant/{tenantId}/user/resetpass'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request <strong>sets the multi-factor '
                                         'authentication token</strong> of the current '
                                         'authenticated user.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'set_mfa_token',
                          'name': 'Set MFA Token',
                          'path': '/api/v1/user/mfa/token'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [],
                          'description': '<p>This request <strong>disables the multi-factor '
                                         'authentication token</strong> of the current '
                                         'authenticated user.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'disable_user_mfa_token',
                          'name': 'Disable User MFA Token',
                          'path': '/api/v1/user/mfa/token/disable'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Disable MFA for an authorized user in your '
                                         'tenant</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'disable_other_user_mfa_token',
                          'name': 'Disable Other User MFA Token',
                          'path': '/api/v1/tenant/{tenantId}/user/mfa/disable'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Toggles the <strong>User Disabled</strong> switch '
                                         'shown in the Admin Dashboard &gt; Users. This enables or '
                                         'disables a user from authenticating to the '
                                         'platform.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'enable_disable_user',
                          'name': 'Enable/Disable User',
                          'path': '/api/v1/tenant/{tenantId}/user/toggledisabled'},
                         {'aliases': [],
                          'body_mode': 'none',
                          'default_params': [('limit', '10'), ('skip', '0'), ('read', 'unread')],
                          'description': '<p>This request <strong>retrieves notifications</strong> '
                                         'for the current authenticated user.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'GET',
                          'method_name': 'get_user_notifications',
                          'name': 'Get User Notifications',
                          'path': '/api/v1/user/notifications'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>Mark a notification as read by the user.</p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'PUT',
                          'method_name': 'set_user_notifications_read',
                          'name': 'Set User Notifications Read',
                          'path': '/api/v1/user/notifications'},
                         {'aliases': [],
                          'body_mode': 'raw',
                          'default_params': [],
                          'description': '<p>This request <strong>retrieves a list of findings '
                                         'assigned to the user making the API call.</strong></p>\n',
                          'folder_path': ['Users'],
                          'graphql_query': None,
                          'method': 'POST',
                          'method_name': 'get_user_findings',
                          'name': 'Get User Findings',
                          'path': '/api/v2/user/findings'}]},
 'webhooks': {'display_name': 'Webhooks',
              'endpoints': [{'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This webhook event is triggered whenever a report '
                                            'finding is created or edited. This event should fire '
                                            'for any method of finding creation or editting, '
                                            'including findings pulled into a report from the '
                                            'WriteupsDB, file import, or an integration; or when '
                                            'the finding is edited via the edit side drawer, any '
                                            'bulk options, or other WFA that makes changes to a '
                                            'finding. When this event fires, PlexTrac sends a POST '
                                            'request containing the event payload to your '
                                            'configured webhook URL.</p>\n'
                                            "<p>If you've specified a secret during the webhook "
                                            'setup in the PlexTrac UI, an '
                                            '<strong><code>x-authorization-hmac-256</code></strong> '
                                            'header will be included with a signature, allowing '
                                            'you to verify the authenticity of the incoming '
                                            'request.</p>\n'
                                            '<p>This request can act as a test to verify your '
                                            'listener is setup properly to recieve the event form '
                                            'PlexTrac.</p>\n'
                                            '<h3 id="finding-the-related-report-finding">Finding '
                                            'the Related Report Finding</h3>\n'
                                            '<p>This event provides the clientId, reportId, and '
                                            'findingId related to the created/editted finding. To '
                                            'retrieve the full details of this report finding you '
                                            'can use the <strong><code>GET '
                                            '/api/v1/client/{clientId}/report/{reportId}/flaw{findingId}</code></strong> '
                                            'endpoint. Refer to the documentation for the '
                                            '<strong>GET Finding</strong> request for more '
                                            'details.</p>\n',
                             'folder_path': ['Webhooks', 'Workflow Automations'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'wfa_on_report_finding_creation_edit',
                             'name': 'WFA: On Report Finding Creation/Edit',
                             'path': 'https://[YOUR_WEBHOOK_LISTENER_URL]'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>This webhook event is triggered whenever a report '
                                            'is created or edited. This event should fire for any '
                                            'method of report creation or editting, including '
                                            'manual creation, submission of an Assessment/Runbook, '
                                            'or using the Scheduler; or when the report is edited '
                                            'via the Details page, any bulk options, or other WFA '
                                            'that makes changes to a report. When this event '
                                            'fires, PlexTrac sends a POST request containing the '
                                            'event payload to your configured webhook URL.</p>\n'
                                            "<p>If you've specified a secret during the webhook "
                                            'setup in the PlexTrac UI, an '
                                            '<strong><code>x-authorization-hmac-256</code></strong> '
                                            'header will be included with a signature, allowing '
                                            'you to verify the authenticity of the incoming '
                                            'request.</p>\n'
                                            '<p>This request can act as a test to verify your '
                                            'listener is setup properly to recieve the event form '
                                            'PlexTrac.</p>\n'
                                            '<h3 id="finding-the-related-report">Finding the '
                                            'Related Report</h3>\n'
                                            '<p>This event provides the <strong>clientId</strong> '
                                            'and <strong>reportId</strong> related to the '
                                            'created/editted report. To retrieve the full details '
                                            'of this report you can use the <strong><code>GET '
                                            '/api/v1/client/{clientId}/report/{reportId}</code></strong> '
                                            'endpoint. Refer to the documentation for the '
                                            '<strong>GET Report</strong> request for more '
                                            'details.</p>\n',
                             'folder_path': ['Webhooks', 'Workflow Automations'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'wfa_on_report_creation_edit',
                             'name': 'WFA: On Report Creation/Edit',
                             'path': 'https://[YOUR_WEBHOOK_LISTENER_URL]'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>The <code>ReportPublished</code> webhook event is '
                                            "triggered whenever a report's status changes from any "
                                            'non-published state to <code>Published</code>. When '
                                            'this event fires, PlexTrac sends a POST request '
                                            'containing the event payload to your configured '
                                            'webhook URL.</p>\n'
                                            "<p>If you've specified a secret during the webhook "
                                            'setup in the PlexTrac UI, an '
                                            '<strong><code>x-authorization-hmac-256</code></strong> '
                                            'header will be included with a signature, allowing '
                                            'you to verify the authenticity of the incoming '
                                            'request.</p>\n'
                                            '<p>This request can act as a test to verify your '
                                            'listener is setup properly to recieve the event form '
                                            'PlexTrac.</p>\n'
                                            '<h3 id="finding-the-related-report">Finding the '
                                            'Related Report</h3>\n'
                                            '<p>The <code>ReportPublished</code> event provides '
                                            'the <code>targetCuid</code> for the report that was '
                                            'published. To retrieve the full details of this '
                                            'report using its <code>cuid</code>, you can use the '
                                            '<strong><code>POST /api/v2/reports</code></strong> '
                                            'endpoint. This API allows you to filter reports by '
                                            '<code>cuids</code> to get the specific report object. '
                                            'Refer to the documentation for the <a '
                                            'href="https://api-docs.plextrac.com/#2af4bc8d-6369-4604-ae79-af0b22785179">POST '
                                            '/api/v2/reports</a> request for more details.</p>\n',
                             'folder_path': ['Webhooks'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'on_report_published',
                             'name': 'On Report Published',
                             'path': 'https://[YOUR_WEBHOOK_LISTENER_URL]'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>The <code>FindingPublished</code> webhook event '
                                            "triggers whenever a finding's status is moved to "
                                            '<code>Published</code> within PlexTrac. When this '
                                            'event fires, PlexTrac sends a POST request containing '
                                            'the event payload to your configured webhook '
                                            'URL.</p>\n'
                                            "<p>If you've specified a secret during the webhook "
                                            'setup in the PlexTrac UI, an '
                                            '<code>x-authorization-hmac-256</code> header will be '
                                            'included with a signature, allowing you to verify the '
                                            'authenticity of the incoming request.</p>\n'
                                            '<p>This request can also act as a test to verify your '
                                            'listener is set up properly to receive the event from '
                                            'PlexTrac.</p>\n'
                                            '<h3 '
                                            'id="finding-the-related-report-and-finding">Finding '
                                            'the Related Report and Finding</h3>\n'
                                            '<p>This webhook payload provides the '
                                            '<strong><code>clientId</code></strong>, '
                                            '<strong><code>reportId</code></strong>, and '
                                            '<strong><code>findingId</code></strong>.</p>\n'
                                            '<p>The most efficient way to get a single finding is '
                                            'using the <a '
                                            'href="https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc">GET '
                                            '/api/v1/client/{clientId}/report/{reportId}/flaw/{findingId}</a> '
                                            'endpoint.</p>\n',
                             'folder_path': ['Webhooks'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'on_report_finding_published',
                             'name': 'On Report Finding Published',
                             'path': 'https://[YOUR_WEBHOOK_LISTENER_URL]'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>The <code>AssessmentSubmitted</code> webhook event '
                                            'is triggered whenever an assessment is submitted to '
                                            'become a report. This process <strong>automatically '
                                            'generates a new report</strong>, where each '
                                            'assessment question is converted into a finding. '
                                            'After an assessment is submitted, it is no longer '
                                            'editable and the report becomes the main record of '
                                            'the assessment.</p>\n'
                                            '<p>When this event fires, PlexTrac sends a POST '
                                            'request containing the event payload to your '
                                            'configured webhook URL.</p>\n'
                                            "<p>If you've specified a secret during the webhook "
                                            'setup in the PlexTrac UI, an '
                                            '<strong><code>x-authorization-hmac-256</code></strong> '
                                            'header will be included with a signature, allowing '
                                            'you to verify the authenticity of the incoming '
                                            'request.</p>\n'
                                            '<p>This request can act as a test to verify your '
                                            'listener is setup properly to recieve the event form '
                                            'PlexTrac.</p>\n'
                                            '<h3 id="finding-the-related-report">Finding the '
                                            'Related Report</h3>\n'
                                            '<p>This webhook payload provides the '
                                            '<strong><code>clientId</code></strong> and '
                                            '<strong><code>reportId</code></strong>, which are '
                                            'essential for retrieving the newly generated report. '
                                            'The most efficient way to get a single report is '
                                            'using the <strong><code>GET '
                                            '/api/v1/client/{clientId}/report/{reportId}</code></strong> '
                                            'endpoint.</p>\n',
                             'folder_path': ['Webhooks'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'on_assessment_submission',
                             'name': 'On Assessment Submission',
                             'path': 'https://[YOUR_WEBHOOK_LISTENER_URL]'},
                            {'aliases': [],
                             'body_mode': 'raw',
                             'default_params': [],
                             'description': '<p>The <code>SchedulerEngagementSubmitted</code> '
                                            'webhook event triggers whenever a scheduled '
                                            'engagement is created within PlexTrac. This event '
                                            'typically signifies that an engagement has been '
                                            'finalized or confirmed via the scheduler.</p>\n'
                                            '<p>When this event fires, PlexTrac sends a POST '
                                            'request containing the event payload to your '
                                            'configured webhook URL.</p>\n'
                                            "<p>If you've specified a secret during the webhook "
                                            'setup in the PlexTrac UI, an '
                                            '<code>x-authorization-hmac-256</code> header will be '
                                            'included with a signature, allowing you to verify the '
                                            'authenticity of the incoming request.</p>\n'
                                            '<p>This request can also act as a test to verify your '
                                            'listener is set up properly to receive the event from '
                                            'PlexTrac.</p>\n'
                                            '<h3 '
                                            'id="finding-the-related-scheduler-engagement">Finding '
                                            'the Related Scheduler Engagement</h3>\n'
                                            '<p>This webhook payload provides the '
                                            '<strong><code>targetCuid</code></strong> for the '
                                            'submitted engagement. To retrieve the full details of '
                                            'this engagement, you can use the direct endpoint: <a '
                                            'href="https://api-docs.plextrac.com/#a615ea61-8aab-47b7-9874-b254183fbf23">GET '
                                            '/api/v2/engagement-schedule-events/{{engagementScheduleEventCuid}}</a>. '
                                            'Simply replace '
                                            '<code>{{engagementScheduleEventCuid}}</code> with the '
                                            '<code>targetCuid</code> from the webhook '
                                            'payload.</p>\n',
                             'folder_path': ['Webhooks'],
                             'graphql_query': None,
                             'method': 'POST',
                             'method_name': 'on_scheduler_engagement_submission',
                             'name': 'On Scheduler Engagement Submission',
                             'path': 'https://[YOUR_WEBHOOK_LISTENER_URL]'}]}}
