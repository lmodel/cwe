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
  One aspect of a weakness, or of how two weaknesses differ, named in a word or two.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweDimension  {

  private String type;
  private String value;


}