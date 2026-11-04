package example;

/* metamodel_version: 1.12.0 */
/* version: 5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A source that entries of the catalogue cite, such as a paper, a book or a web page.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweExternalReference  {

  private String referenceID;
  private List<String> author;
  private String title;
  private String edition;
  private String publication;
  private String publicationYear;
  private String publicationMonth;
  private String publicationDay;
  private String publisher;
  private URI uRL;
  private LocalDate uRLDate;
  private URI altURL;
  private LocalDate altURLDate;
  private List<String> mediaType;
  private String accessRestrictions;
  private List<String> rationale;


}