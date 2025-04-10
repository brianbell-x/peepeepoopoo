# OpenAI GPT-4o Responses API Documentation

*(...existing content preserved above...)*

---

# Appendix: Detailed Parameter Reference

## Input Types

### `input` (string or array) **Required**

- **Text input (string):** Equivalent to a user message.
- **Array of input items:** Each item can be:

---

### Input Item Types

#### Text Input (string)

```json
"Hello, world!"
```

#### Input Message (object)

```json
{
  "role": "user",
  "content": [ ... ],
  "type": "message" // optional, defaults to message
}
```

- `role` **Required:** `"user"`, `"assistant"`, `"system"`, `"developer"`
- `content` **Required:** array of input items (text, image, file, audio, previous assistant responses)
- `type` *Optional:* `"message"`

---

### Input Item Content Types

#### Text Input (object)

```json
{
  "type": "input_text",
  "text": "Hello"
}
```

- `type` **Required:** `"input_text"`
- `text` **Required:** string

#### Image Input (object)

```json
{
  "type": "input_image",
  "detail": "auto", // "high", "low", or "auto" (default)
  "file_id": "file-abc123", // optional
  "image_url": "https://..." // optional, or base64 data URL
}
```

- `type` **Required:** `"input_image"`
- `detail` **Required:** `"high"`, `"low"`, `"auto"` (default)
- `file_id` *Optional:* string or null
- `image_url` *Optional:* string or null

#### File Input (object)

```json
{
  "type": "input_file",
  "file_data": "...", // optional
  "file_id": "file-abc123", // optional
  "filename": "document.pdf" // optional
}
```

- `type` **Required:** `"input_file"`
- `file_data` *Optional:* string
- `file_id` *Optional:* string
- `filename` *Optional:* string

---

## Message Roles

- `"user"`
- `"assistant"`
- `"system"`
- `"developer"`

---

## Response Object

- `id` **Required:** string
- `object` **Required:** `"response"`
- `created_at` **Required:** Unix timestamp (seconds)
- `status` **Required:** `"completed"`, `"in_progress"`, `"failed"`, `"incomplete"`
- `error` *Optional:* error object or null
- `instructions` *Optional:* string or null
- `max_output_tokens` *Optional:* integer or null
- `model` **Required:** string
- `output` **Required:** array of output messages
- `parallel_tool_calls` **Required:** boolean
- `previous_response_id` *Optional:* string or null
- `reasoning` *Optional:* object or null
- `store` **Required:** boolean
- `temperature` *Optional:* number or null
- `text` *Optional:* object
- `tool_choice` *Optional:* string or object
- `tools` *Optional:* array
- `top_p` *Optional:* number or null
- `truncation` *Optional:* string or null
- `usage` *Optional:* object
- `user` *Optional:* string or null
- `metadata` *Optional:* map

---

## Output Message Object

- `type` **Required:** `"message"`
- `id` **Required:** string
- `status` **Required:** `"completed"`, `"in_progress"`, `"incomplete"`
- `role` **Required:** `"assistant"`
- `content` **Required:** array of content items

### Content Item Types

#### Output Text

```json
{
  "type": "output_text",
  "text": "...",
  "annotations": []
}
```

- `type` **Required:** `"output_text"`
- `text` **Required:** string
- `annotations` **Required:** array of annotations

#### Refusal

```json
{
  "type": "refusal",
  "refusal": "Explanation"
}
```

- `type` **Required:** `"refusal"`
- `refusal` **Required:** string

#### File Citation

```json
{
  "type": "file_citation",
  "file_id": "...",
  "index": 0
}
```

- `type` **Required:** `"file_citation"`
- `file_id` **Required:** string
- `index` **Required:** integer

#### URL Citation

```json
{
  "type": "url_citation",
  "url": "...",
  "title": "...",
  "start_index": 0,
  "end_index": 10
}
```

- `type` **Required:** `"url_citation"`
- `url` **Required:** string
- `title` **Required:** string
- `start_index` **Required:** integer
- `end_index` **Required:** integer

---

## Tool Call Objects

### File Search Tool Call

- `id` **Required:** string
- `queries` **Required:** array
- `status` **Required:** `"in_progress"`, `"searching"`, `"incomplete"`, `"failed"`
- `type` **Required:** `"file_search_call"`
- `results` *Optional:* array or null
- `attributes`, `file_id`, `filename`, `score`, `text` *Optional*

### Function Tool Call

- `arguments` **Required:** JSON string
- `call_id` **Required:** string
- `name` **Required:** string
- `type` **Required:** `"function_call"`
- `id` *Optional:* string
- `status` *Optional:* `"in_progress"`, `"completed"`, `"incomplete"`

### Function Tool Call Output

- `call_id` **Required:** string
- `output` **Required:** JSON string
- `type` **Required:** `"function_call_output"`
- `id` *Optional:* string
- `status` *Optional:* `"in_progress"`, `"completed"`, `"incomplete"`

---

## Reasoning Object

- `id` **Required:** string
- `summary` **Required:** array of strings
- `type` **Required:** `"reasoning"`
- `status` *Optional:* `"in_progress"`, `"completed"`, `"incomplete"`

---

## Additional Parameters

- `include` *Optional:* array or null  
  Supported values:
  - `file_search_call.results`
  - `message.input_image.image_url`
  - `computer_call_output.output.image_url`

- `parallel_tool_calls` *Optional:* boolean (default: true)
- `stream` *Optional:* boolean (default: false)
- `metadata` *Optional:* map (up to 16 key-value pairs)
- `user` *Optional:* string (end-user ID)
- `truncation` *Optional:* `"auto"` or `"disabled"` (default)

---

## Response Streaming

If `stream=true`, the API streams response data as server-sent events.

---

## Supported Tools

- **Built-in:**
  - File Search
  - Web Search
  - Computer Use
- **Custom:**
  - Function Calls (JSON schema-defined)

---

This appendix ensures **all** details from the original API reference are preserved in markdown format.