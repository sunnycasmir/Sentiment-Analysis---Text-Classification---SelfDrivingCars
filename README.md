This is a reseach study that delved into public perceptions of self-driving cars, analyzing a Twitter dataset of 28,893 tweets.
Employing preprocessing techniques like deduplication, HTML tag removal, lemmatization, and tokenization, prevalent themes such as safety and innovation emerge through WordCloud exploratory analysis. 
Classical machine learning models, particularly Gradient Boosting with bag-of-words, achieve about 75% balanced accuracy, excelling at 84% accuracy and a robust 0.95 negative recall.
In deep learning, LSTM, BiLSTM, and BERT models exhibit notable performance, with BERT showcasing 91% accuracy and >0.89 precision and recall. 
Outperforming benchmarks, these findings provide predictive models that are capable to provide actionable insights for automakers and regulators, emphasizing BERT's efficacy in capturing nuanced sentiments amid evolving autonomous technologies.
App for model was also built and deployed using streamlit. Although BERT model performed better. However, for deployment, Lstm model was choosed because it was discovered to be lighter and faster when tested on the app.
Future research recommendations include dataset expansion, neural architecture refinement, and broader application for mining internet users' opinions on self-driving cars.
