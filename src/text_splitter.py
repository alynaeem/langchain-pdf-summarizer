class RecursiveCharacterTextSplitter:

    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = ["\n\n", "\n", " ", ""]

    def split_text(self, text, separators=None):
        separators = separators or self.separators
        separator = separators[-1]
        new_separators = []

        for i, sep in enumerate(separators):
            if sep == "":
                separator = ""
                break

            if sep in text:
                separator = sep
                new_separators = separators[i + 1 :]
                break

        if separator:
            splits = text.split(separator)
        else:
            splits = list(text)

        final_chunks = []
        current_chunk = []
        
        for split in splits:
            split_len = len(split)

            if split_len > self.chunk_size:
                if current_chunk:
                    doc = separator.join(current_chunk)
                    final_chunks.append(doc)
                    current_chunk = []
                    
                if new_separators:
                    sub_chunks = self.split_text(split, separators=new_separators)
                    final_chunks.extend(sub_chunks)
                else:
                    final_chunks.append(split)
                continue

            combined_text = separator.join(current_chunk + [split])
            
            if len(combined_text) > self.chunk_size:
                final_chunks.append(separator.join(current_chunk))
                
                while len(separator.join(current_chunk)) > self.chunk_overlap:
                    if not current_chunk:
                        break
                    current_chunk.pop(0)

            current_chunk.append(split)

        if current_chunk:
            final_chunks.append(separator.join(current_chunk))

        return final_chunks